from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course


class CourseListView(ListView):
    model = Course
    template_name = 'courses/courses-list.html'
    context_object_name = 'courses'


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/courses-detail.html'
    context_object_name = 'course'



