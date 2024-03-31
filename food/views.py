from django.shortcuts import render  # Importing render function from Django's shortcuts module
from django.views import View  # Importing View class from Django's views module

# Defining a view for displaying information about food
class Food(View):
    def get(self, request):
        return render(request, 'food/food.html')  # Rendering the food.html template
