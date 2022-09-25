from django.urls import reverse
from django.utils import timezone
from django.db import models
from tinymce.models import HTMLField
from courses.models import Teacher


class Blog(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='creator')
    image = models.ImageField(upload_to='images/blogs', null=True)
    views = models.IntegerField(default=0)
    description = HTMLField()
    status = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.pk])

    def __str__(self):
        return f"{self.title} - {self.author} - {self.status}"
