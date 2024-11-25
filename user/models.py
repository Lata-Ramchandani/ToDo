from django.db import models
from django.contrib.auth.models import User
# from .forms import UserResgistrationForm
# Create your models here.

class UserProfile(models.Model):
    # username = models.CharField(max_length=20)
    # email = models.EmailField(max_length=20)
    # password = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username