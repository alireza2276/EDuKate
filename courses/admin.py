from django.contrib import admin
from .models import Course, Teacher, Category


admin.site.register(Teacher)
admin.site.register(Category)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'status']

