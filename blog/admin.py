from django.contrib import admin
from .models import Blog
from jalali_date.admin import ModelAdminJalaliMixin


@admin.register(Blog)
class BlogAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'author', 'status']
