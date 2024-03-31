from django.urls import path  # Importing the path function from Django's URL module

from .views import TravelTips  # Importing the TravelTips view from the current application's views module

# URL patterns for the application
urlpatterns = [
    path('', TravelTips.as_view(), name='traveltips'),  # Mapping the root URL to the TravelTips view
]
