# Import necessary modules and classes from Django
from django import forms

# Import the Comment model from the current application
from .models import Comment

# Define a form for adding comments to an article
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': ''}
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Add a comment...', 'rows': 4})
        }

        def clean_text(self):
            text = self.cleaned_data['text']
            if len(text.strip()) == 0:
                raise ValidationError('Comment cannot be empty.')
            return text
