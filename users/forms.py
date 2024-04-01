from django import forms  # Importing forms module from Django
from django.contrib.auth.models import User  # Importing User model from Django's built-in authentication system
from django.contrib.auth.forms import UserCreationForm  # Importing UserCreationForm for user registration
from .models import UserProfile

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()  # Adding email field to the form

	class Meta:
		model = User  # Setting the model to User
		fields = ['username', 'email', 'password1', 'password2']  # Specifying the fields for the form


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'bio', 'travel_interests', 'profile_picture']