from django.urls import path  # Importing path function from Django's URL module
from .views import ContactView  # Importing ContactView from the current application's views module
from django.contrib.auth import views as auth_views  # Importing auth_views from Django's authentication views

# URL patterns for the application
urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),  # Mapping the contact URL to the ContactView
]
