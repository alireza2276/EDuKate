from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView

from .forms import CommentForm
from .models import Course, Category, Teacher, Comment


class CourseListView(ListView):
    model = Course
    template_name = 'courses/courses-list.html'
    context_object_name = 'courses'
    paginate_by = 3


# class CourseDetailView(DetailView):
#     model = Course
#     template_name = 'courses/courses-detail.html'
#     context_object_name = 'course'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['comment_form'] = CommentForm()
#         return context


def course_detail(request, pk):
    course = get_object_or_404(Course, id=pk)
    if request.method == 'POST':
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(body=body, course=course, author=request.user, parent_id=parent_id)
    return render(request, 'courses/courses-detail.html', context={'course': course})


def category(request, pk=None):
    categories = get_object_or_404(Category, id=pk)
    courses = categories.categories.all()
    return render(request, 'courses/courses-list.html', {'categories': categories, 'courses': courses})


class TeacherListView(ListView):
    model = Teacher
    template_name = 'courses/teacher-list.html'
    context_object_name = 'teachers'


class CommentCreateView(CreateView, LoginRequiredMixin):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        course_id = int(self.kwargs['course_id'])
        course = get_object_or_404(Course, id=course_id)
        obj.course = course

        return super().form_valid(form)
