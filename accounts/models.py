from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.

class ProfilePic(models.Model):
    name = models.ForeignKey(User)
    profilephoto = models.ImageField(upload_to = 'proPhotos',blank = False)

    def __str__(self):
        return self.name.username

    def get_absolute_url(self):
        return reverse("test")
