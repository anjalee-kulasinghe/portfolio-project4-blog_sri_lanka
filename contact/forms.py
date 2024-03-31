from django import forms  # Importing forms module from Django

# Defining a contact form
class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)  # Name field
    email = forms.EmailField(label='Your Email')  # Email field
    message = forms.CharField(label='Your Message', widget=forms.Textarea)  # Message field with Textarea widget
