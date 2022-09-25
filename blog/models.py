from django.urls import reverse
from django.utils import timezone
from django.db import models
from tinymce.models import HTMLField
from courses.models import Teacher
from django.utils.translation import gettext_lazy as _


class Blog(models.Model):
    title = models.CharField(_('title'), max_length=50)
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='creator', verbose_name=_('author'))
    image = models.ImageField(_('image'), upload_to='images/blogs', null=True)
    views = models.IntegerField(_('view'), default=0)
    description = HTMLField(_('description'))
    status = models.BooleanField(_('status'), default=True)

    datetime_created = models.DateTimeField(_('datetime_created'), default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = _('Blogs')

    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.pk])

    def __str__(self):
        return f"{self.title} - {self.author} - {self.status}"
