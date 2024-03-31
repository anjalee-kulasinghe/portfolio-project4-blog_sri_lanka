from django.urls import path  # Importing the path function from Django's URL module
from .views import CityGuide  # Importing the CityGuide view from the current application's views module

urlpatterns = [
    path('', CityGuide.as_view(), name='cityguide'),  # Mapping the empty path to the CityGuide view
]
