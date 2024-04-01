from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import UserProfile

"""
Creating a registration form
to register new users
"""
class RegisterView(View):
    # Handling GET requests to display the registration form
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    # Handling POST requests to process form submission
    def post(self, request):
        form = UserRegisterForm(request.POST)

        # Check if the form data is valid
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully! Please log in.')
            return redirect('login')
        else:
            # If form data is invalid, render the registration form template with the form and errors
            return render(request, 'users/register.html', {'form': form})


"""
Create a view to users to complete their account
"""
class CreateProfileView(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'users/create_profile.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UserEditView(UpdateView):
    form_class = UserProfileForm
    template_name = 'users/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user