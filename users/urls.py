from django.urls import path  # Importing path function from django.urls
from .views import RegisterView, UserEditView, CreateProfileView  # Importing RegisterView from the current directory views module
from django.contrib.auth import views as auth_views  # Importing authentication views as auth_views
from .views import UserProfile

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # URL pattern for user registration
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),  # URL pattern for user login
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),  # URL pattern for user logout
    path('create_profile/', CreateProfileView.as_view(), name='create_profile'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
]
