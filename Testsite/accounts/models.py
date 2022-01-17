from django.db import models
from django.contrib.auth.models import User
from PIL import Image
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
    
    def save(self):
        super().save()
        self.resize_uploaded_image()
    
    def resize_uploaded_image(self):
        img = Image.open(self.profile_picture.path) ##Open profile picture!
        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size) # Resize the picture
            img.save(self.profile_picture.path) # Save and override the current picture.
    
    def get_list_of_traits(self):
        return self.traits.split(',')
    