from .models import Comment, Post
from django import forms


# Form for the Comment model
class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea, label='') # Define the body field as a CharField with a Textarea widget and no label
    class Meta: # Specify the model and fields to include in the form
        model = Comment
        fields = ('body',)


# Form for the Post model
class PostForm(forms.ModelForm):
    class Meta: # Specify the model and fields to include in the form
        model = Post
        fields = ['title', 'body', 'featured_image', 'author_image',]

    # Custom initialization method to set field requirements
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['body'].required = True
        self.fields['featured_image'].required = False
        self.fields['author_image'].required = False


# The code in this file is inspired from:
# My own previous projects and knowledge
# Code Institute, I think therefore i blog project
# Python Django Web Framework (https://www.djangoproject.com/start/overview/)
# Youtube Django Tutorial by [Freecode camp](https://www.youtube.com/watch?v=F5mRW0jo-U4)
# Youtube series Django Tutorial by [Net Ninja](https://www.youtube.com/watch?v=n-FTlQ7Djqc&list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc&index=1&ab_channel=NetNinja)
# Youtube series Python Django Tutorial by [Corey Schafer](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=1&ab_channel=CoreySchafer)
# Yoube Python Django Web Framework by [FreeCodeCamp](https://www.youtube.com/watch?v=F5mRW0jo-U4&ab_channel=freeCodeCamp.org)