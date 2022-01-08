from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name="Owner", on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='default.png', upload_to='profile_pics')
    biography = models.TextField(default="")
    current_job = models.CharField(max_length=50, default="")
    current_goal = models.CharField(max_length=120, default="Be happy!")
    traits = models.CharField(max_length=60, default="")

    def __str__(self):
        return f'{self.user.username}\'s profile!'
    