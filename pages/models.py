from django.db import models


class Information(models.Model):
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    instagram = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.subject}"
