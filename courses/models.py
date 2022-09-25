from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=50)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/teacher', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.title}"


class Course(models.Model):
    category = models.ManyToManyField(Category, related_name='categories')
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='authors')
    image = models.ImageField(upload_to='images/courses', null=True, blank=True)
    price = models.PositiveIntegerField(default=0, null=True, blank=True)
    lectures = models.IntegerField()
    duration = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    description = HTMLField()
    status = models.BooleanField(default=True)
    student = models.ManyToManyField(get_user_model(), related_name='student')

    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('courses_detail', args=[self.pk])

    def __str__(self):
        return f"{self.title} - {self.author} - {self.price}"


class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
    image = models.ImageField(upload_to='images/comments', null=True, blank=True)
    body = HTMLField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    datetime_created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('courses_detail', args=[self.course.id])

    def __str__(self):
        return f"{self.author} - {self.course}"
