from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView, CreateView

from blog.models import Blog
from pages.forms import ContactForm
from pages.models import Contact
from django.urls import reverse_lazy
from courses.models import Course, Teacher


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_courses'] = Course.objects.all()
        context['all_blogs'] = Blog.objects.all()
        context['all_teachers'] = Teacher.objects.all()

        return context





class ContactView(CreateView):
    model = Contact
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')



