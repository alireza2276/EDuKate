from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Course, Category, Teacher


class CourseListView(ListView):
    model = Course
    template_name = 'courses/courses-list.html'
    context_object_name = 'courses'
    paginate_by = 3


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/courses-detail.html'
    context_object_name = 'course'


def category(request, pk=None):
    categories = get_object_or_404(Category, id=pk)
    courses = categories.categories.all()
    return render(request, 'courses/courses-list.html', {'categories': categories, 'courses': courses})


class TeacherListView(ListView):
    model = Teacher
    template_name = 'courses/teacher-list.html'
    context_object_name = 'teachers'
