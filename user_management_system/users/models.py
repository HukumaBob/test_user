from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Additional fields for the user model
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username
