from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import UserProfile

"""
Creating a registration form
to register new users
"""
class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your account has been created successfully! Please log in.')
            return redirect('create_profile')
        else:
            return render(request, 'users/register.html', {'form': form})

"""
Create a view to allow users to complete their account
"""
class CreateProfileView(LoginRequiredMixin, CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'users/create_profile.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UserEditView(LoginRequiredMixin, UpdateView):
    form_class = UserProfileForm
    template_name = 'users/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)
