# Import necessary modules and classes from Django
from django.contrib import admin

# Import the Article model from the current application
from .models import Article

# Register the Article model with the Django admin interface
admin.site.register(Article)
