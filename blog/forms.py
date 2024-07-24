from django import forms
from .models import Comment
from .models import Article
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

"""
Define a form for adding an article by the user
"""
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'articale_image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

"""
Define a form for adding comments to an article
"""
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
