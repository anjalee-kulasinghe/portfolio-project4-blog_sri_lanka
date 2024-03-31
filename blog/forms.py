# Import necessary modules and classes from Django
from django import forms

# Import the Comment model from the current application
from .models import Comment

# Define a form for adding comments to an article
class CommentForm(forms.ModelForm):
    class Meta:
        # Specify the model to use for the form
        model = Comment

        # Define the fields to include in the form
        fields = ['text']

        # Define labels for the form fields
        labels = {'text': ''}

        # Define widgets to customize the form field's appearance
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Add a comment...', 'rows': 4})
        }
