from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):
    # Create relationship - (don't inherit from user)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # Add any additional attributes you want
    profile_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)


    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User
        return self.user.username # username is default attribute of User
