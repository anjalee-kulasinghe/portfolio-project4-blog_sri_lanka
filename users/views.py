from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm


class RegisterView(View):
    # Handling GET requests to display the registration form
    def get(self, request):
        # Instantiate the UserRegisterForm
        form = UserRegisterForm()
        # Render the registration form template with the form object
        return render(request, 'users/register.html', {'form': form})

    # Handling POST requests to process form submission
    def post(self, request):
        # Instantiate the UserRegisterForm with the form data from the POST request
        form = UserRegisterForm(request.POST)

        # Check if the form data is valid
        if form.is_valid():
            # Save the form data to create a new user
            form.save()
            # Display a success message
            messages.success(request, 'Your account has been created successfully! Please log in.')
            # Redirect the user to the login page
            return redirect('login')
        else:
            # If form data is invalid, render the registration form template with the form and errors
            return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'users/profile.html', {'form': form})