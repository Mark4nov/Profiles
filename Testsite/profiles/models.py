from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, verbose_name="Owner", on_delete=models.CASCADE)
    biography = models.TextField(default="")
    current_job = models.CharField(max_length=50, default="")
    current_goal = models.CharField(max_length=120, default="")
    traits = models.CharField(max_length=60, default="")
