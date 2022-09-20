from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseListView.as_view(), name='courses_list'),
    path('<int:pk>/', views.course_detail, name='courses_detail'),
    path('category/<int:pk>/', views.category, name='category'),
    path('teachers/', views.TeacherListView.as_view(), name='teachers_list'),
    path('comment/<int:course_id>/', views.CommentCreateView.as_view(), name='create_comment'),

]
