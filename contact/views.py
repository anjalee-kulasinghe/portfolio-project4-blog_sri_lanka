from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactForm
from .models import Contact


class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact/contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return render(request, 'contact/success.html')
        else:
            return render(request, 'contact/contact.html', {'form': form})

