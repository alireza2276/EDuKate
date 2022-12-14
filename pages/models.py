from django.db import models
from django.utils.translation import gettext_lazy as _


class Information(models.Model):
    address = models.CharField(_('address'), max_length=200)
    phone = models.CharField(_('phone'), max_length=15)
    email = models.EmailField(_('email'))
    instagram = models.CharField(_('instagram'), max_length=50)
    linkedin = models.CharField(_('linkedin'), max_length=50)

    class Meta:
        verbose_name_plural = _('information')


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    subject = models.CharField(max_length=100, verbose_name=_('subject'))
    body = models.TextField(verbose_name=_('body'))

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        verbose_name_plural = _('contact')
