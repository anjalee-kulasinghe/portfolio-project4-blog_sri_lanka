from django.shortcuts import render  # Importing render function from Django's shortcuts module
from django.views import View  # Importing View class from Django's views module

# Defining a view for displaying the city guide
class CityGuide(View):
    def get(self, request):
        return render(request, 'cityguide/cityguide.html')  # Rendering the city guide template
