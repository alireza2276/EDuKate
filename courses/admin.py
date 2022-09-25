from django.contrib import admin
from .models import Course, Teacher, Category, Comment
from jalali_date.admin import ModelAdminJalaliMixin
admin.site.register(Teacher)
admin.site.register(Category)


@admin.register(Course)
class CourseAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'status']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'course', 'datetime_created', ]

