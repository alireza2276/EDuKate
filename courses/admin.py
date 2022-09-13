from django.contrib import admin
from .models import Course, Teacher


admin.site.register(Teacher)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'status']

