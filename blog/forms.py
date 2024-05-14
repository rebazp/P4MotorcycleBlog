from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'featured_image', 'author_image',]

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['body'].required = True
        self.fields['featured_image'].required = False
        self.fields['author_image'].required = False