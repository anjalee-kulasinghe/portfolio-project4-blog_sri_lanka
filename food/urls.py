from django.urls import path  # Importing path function from Django's URL module
from .views import Food  # Importing Food view from the current application's views module

# URL patterns for the application
urlpatterns = [
    path('', Food.as_view(), name='food'),  # Mapping the root URL to the Food view
]
