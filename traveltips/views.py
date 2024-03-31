from django.shortcuts import render  # Importing the render function from Django's shortcuts module
from django.views import View  # Importing the View class from Django's views module

# Defining a view for displaying travel tips
class TravelTips(View):
    def get(self, request):
        return render(request, 'traveltips/traveltips.html')  # Rendering the traveltips.html template
