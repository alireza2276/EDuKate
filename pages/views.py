from django.contrib import messages
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView, CreateView
from pages.forms import ContactForm
from pages.models import Contact
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = 'pages/home.html'


class ContactView(CreateView):
    model = Contact
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')




