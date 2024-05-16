from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.utils.text import slugify


# Define choices for the status field
STATUS = ((0, "Draft"), (1, "Published"))


# Model representing a blog post
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True) # Title of the post, must be unique
    body = models.TextField(default='') # Body of the post
    slug = models.SlugField(max_length=200, unique=True) # URL-friendly slug, must be unique
    author = models.ForeignKey( # Author of the post, linked to the User model
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder') # Featured image for the post, stored using Cloudinary
    author_image = CloudinaryField('image', default='placeholder', blank=True, null=True) # Author's profile image, stored using Cloudinary, optional field
    excerpt = models.TextField(blank=True) # Excerpt of the post
    updated_on = models.DateTimeField(auto_now=True) # Timestamp of the last update
    created_on = models.DateTimeField(auto_now_add=True) # Timestamp of post creation
    status = models.IntegerField(choices=STATUS, default=1) # Status of the post (draft or published)
    likes = models.ManyToManyField( # Users who liked the post, many-to-many relationship
        User, related_name='blogpost_like', blank=True)

    # Meta class to define additional settings
    class Meta:
        ordering = ["-created_on"]

    # Override the save method to auto-generate slug from title if not provided
    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    # String representation of the model
    def __str__(self):
        return self.title

    # Method to count the number of likes for a post
    def number_of_likes(self):
        return self.likes.count()

    # Method to get the absolute URL of a post
    def get_absolute_url(self):
        return reverse('home')


# Model representing a comment on a blog post
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, # The post the comment is related to
                             related_name="comments")
    name = models.CharField(max_length=80) # Name of the person who commented
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None) # User who commented, linked to the User model
    email = models.EmailField() # Email of the person who commented
    body = models.TextField() # Body of the comment
    created_on = models.DateTimeField(auto_now_add=True) # Timestamp of comment creation
    approved = models.BooleanField(default=True) # Approval status of the comment

    # Meta class to define additional settings
    class Meta:
        ordering = ["created_on"] # Order comments by creation date in ascending order

    # String representation of the model
    def __str__(self):
        return f"Comment {self.body} by {self.name}"


# The code in this file is inspired from:
# My own previous projects and knowledge
# Code Institute, I think therefore i blog project
# Youtube series Django Tutorial by [Net Ninja](https://www.youtube.com/watch?v=n-FTlQ7Djqc&list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc&index=1&ab_channel=NetNinja)
# Youtube series Python Django Tutorial by [Corey Schafer](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=1&ab_channel=CoreySchafer)
# Yoube Python Django Web Framework by [FreeCodeCamp](https://www.youtube.com/watch?v=F5mRW0jo-U4&ab_channel=freeCodeCamp.org)