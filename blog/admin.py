from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register the Post model with the admin site using a customized admin class
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin interface options for the Post model.
    Inherits from SummernoteModelAdmin to enable rich text editing.
    """
    list_display = ('title', 'slug', 'status', 'created_on') # Fields to display in the admin list view
    search_fields = ['title', 'content'] # Fields to include in the search functionality
    list_filter = ('status', 'created_on') # Filters to allow easy narrowing down of the list view
    prepopulated_fields = {'slug': ('title',)} # Automatically populate the slug field based on the title field
    summernote_fields = ('content',) # Enable Summernote editor for the content field


# Register the Comment model with the admin site using a customized admin class
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin interface options for the Comment model.
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved') # Fields to display in the admin list view
    list_filter = ('approved', 'created_on') # Filters to allow easy narrowing down of the list view
    search_fields = ('name', 'email', 'body') # Fields to include in the search functionality
    actions = ['approve_comments'] # Custom actions available in the admin interface
    
    # Define the custom action to approve comments
    def approve_comments(self, request, queryset): # Action to approve selected comments
        queryset.update(approved=True)

# The code in this file is inspired from:
# My own previous projects and knowledge
# Code Institute, I think therefore i blog project
# Youtube series Django Tutorial by [Net Ninja](https://www.youtube.com/watch?v=n-FTlQ7Djqc&list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc&index=1&ab_channel=NetNinja)
# Youtube series Python Django Tutorial by [Corey Schafer](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=1&ab_channel=CoreySchafer)
# Yoube Python Django Web Framework by [FreeCodeCamp](https://www.youtube.com/watch?v=F5mRW0jo-U4&ab_channel=freeCodeCamp.org)