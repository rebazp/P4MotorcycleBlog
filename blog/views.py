from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect, Http404
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# These are the views and functions that are avilable on specific pages in the blog.
# View for listing blog posts
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


# View for displaying a single post with its details and comments
class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False

        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )
    
    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1) # Get the post based on the slug
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on") # Get approved comments for the post
        liked = False

        if post.likes.filter(id=self.request.user.id).exists(): # Check if the post is liked by the current user
            liked = True

        comment_form = CommentForm(data=request.POST)

        # Validate the comment form and set fields for the comment
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            messages.success(request, 'Your comment has been added!')
        else:
            messages.error(request, 'There was an error adding your comment!')

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": CommentForm(),
                "liked": liked,
            },
        )


# View for handling likes on a post
class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug) # Get the post based on the slug

        if post.likes.filter(id=request.user.id).exists(): # Toggle the like status for the current user
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# View for listing posts, requires user to be logged in
class PostListView(generic.ListView, LoginRequiredMixin):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "post_list.html"
    paginate_by = 6


# View for adding a new post, requires user to be logged in
class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user # Set the author and images for the post
        form.instance.featured_image = self.request.FILES.get('featured_image')
        form.instance.author_image = self.request.FILES.get('author_image')
        form.save()
        messages.success(self.request, 'Your post has been created')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_list')


# View for updating an existing post, requires user to be logged in
class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = PostForm
    success_url = reverse_lazy('post_list')  

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != self.request.user: # Ensure the user is the author of the post
            messages.error(self.request, 'Sorry, you are not authorized to update this post.')
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user # Update the author and images for the post
        form.instance.featured_image = self.request.FILES.get('featured_image')  
        form.instance.author_image = self.request.FILES.get('author_image')  
        messages.success(self.request, 'Your post has been updated')
        return super().form_valid(form)


# View for deleting a post, requires user to be logged in
class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('post_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != self.request.user: # Ensure the user is the author of the post
            messages.error(self.request, 'You are not authorized to delete this post.')
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, 'Your post has been deleted.')
        return HttpResponseRedirect(success_url)


# View for updating a comment, requires user to be logged in
class UpdateCommentView(LoginRequiredMixin, UpdateView):
    model = Comment
    template_name = 'update_comment.html'
    fields = ['body']
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'slug': self.object.post.slug})

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
       
        if self.object.user != self.request.user: # Ensure the user is the author of the comment
            messages.error(self.request, 'You are not authorized to update this comment.')
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Your comment has been updated.')
        return super().form_valid(form)


# Custom login view to handle user authentication
def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if remember: # Set session expiry based on 'remember me' option
                request.session.set_expiry(86400 * 7) # 1 week
            else:
                request.session.set_expiry(0) # Browser session
            messages.success(request, 'You have successfully logged in.')
            return redirect('home') 
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('account_login') 
    else:
        return render(request, 'login.html')


# View for deleting a comment, requires user to be logged in
class DeleteCommentView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'slug': self.object.post.slug})

    def dispatch(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.user != self.request.user: # Ensure the user is the author of the comment
            messages.error(self.request, 'You are not authorized to delete this comment.')
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, 'Your comment has been deleted.')
        return HttpResponseRedirect(success_url)

    
# Custom login view to handle user authentication
def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if remember: # Set session expiry based on 'remember me' option
                request.session.set_expiry(86400 * 7) # 1 week
            else:
                request.session.set_expiry(0) # Browser session
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('account_login')
    else:
        return render(request, 'login.html')


# Custom 404 error handler
def custom_handler404(request, exception):
    
    return render(request, '404.html', status=404)


# Custom 500 error handler
def custom_handler500(request):
    
    return render(request, '500.html', status=500)


# The code in this file is inspired from:
# My own previous projects and knowledge
# Code Institute, I think therefore i blog project
# Python Django Web Framework (https://www.djangoproject.com/start/overview/)
# Youtube Django Tutorial by [Freecode camp](https://www.youtube.com/watch?v=F5mRW0jo-U4)
# Youtube series Django Tutorial by [Net Ninja](https://www.youtube.com/watch?v=n-FTlQ7Djqc&list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc&index=1&ab_channel=NetNinja)
# Youtube series Python Django Tutorial by [Corey Schafer](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=1&ab_channel=CoreySchafer)
# Yoube Python Django Web Framework by [FreeCodeCamp](https://www.youtube.com/watch?v=F5mRW0jo-U4&ab_channel=freeCodeCamp.org)