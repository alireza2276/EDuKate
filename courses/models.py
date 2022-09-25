from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(_('title'), max_length=50)

    datetime_created = models.DateTimeField(_('datetime_created'), auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Category')


class Teacher(models.Model):
    name = models.CharField(_('name'), max_length=50)
    title = models.CharField(_('title'), max_length=50)
    image = models.ImageField(_('image'), upload_to='images/teacher', null=True, blank=True)
    description = models.TextField(_('descriptions'))

    def __str__(self):
        return f"{self.name} - {self.title}"

    class Meta:
        verbose_name_plural = _('Teachers')


class Course(models.Model):
    category = models.ManyToManyField(Category, related_name='categories', verbose_name=_('category'))
    title = models.CharField(_('title'), max_length=50)
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='authors', verbose_name=_('author'))
    image = models.ImageField(_('image'), upload_to='images/courses', null=True, blank=True)
    price = models.PositiveIntegerField(_('price'), default=0, null=True, blank=True)
    lectures = models.IntegerField(_('lectures'))
    duration = models.CharField(_('duration'), max_length=50)
    level = models.CharField(_('level'), max_length=50)
    description = HTMLField(_('descriptions'))
    status = models.BooleanField(_('status'), default=True)
    student = models.ManyToManyField(get_user_model(), related_name='student')

    datetime_created = models.DateTimeField(_('datetime_created'), default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('courses_detail', args=[self.pk])

    def __str__(self):
        return f"{self.title} - {self.author} - {self.price}"

    class Meta:
        verbose_name_plural = _('courses')


class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments',
                               verbose_name=_('author'))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments', verbose_name=_('course'))
    image = models.ImageField(_('image'), upload_to='images/comments', null=True, blank=True)
    body = HTMLField(_('body'))
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies',
                               verbose_name=_('parent'))

    datetime_created = models.DateTimeField(_('datetime_created'), auto_now_add=True)

    def get_absolute_url(self):
        return reverse('courses_detail', args=[self.course.id])

    def __str__(self):
        return f"{self.author} - {self.course}"

    class Meta:
        verbose_name_plural = _('comments')
