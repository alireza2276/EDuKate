from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseListView.as_view(), name='courses_list'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='courses_detail'),
    path('category/<int:pk>/', views.category, name='category'),
    path('teachers/', views.TeacherListView.as_view(), name='teachers_list'),
]