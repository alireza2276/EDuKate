from django.db import models
from tinymce.models import HTMLField


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/teacher', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.title}"


class Course(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='authors')
    image = models.ImageField(upload_to='images/courses', null=True, blank=True)
    price = models.PositiveIntegerField(default=0, null=True, blank=True)
    lectures = models.IntegerField()
    duration = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    description = HTMLField()
    status = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.author} - {self.price}"
