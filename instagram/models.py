from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

    
class Post(models.Model):
    """Post Model."""

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = CloudinaryField('image')
    

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username"""
        return "{} by @{}".format(self.title, self.profile.user.username)
    
class User(models.Model):
    """User model."""



    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    

    bio = models.TextField(blank=True)

    birthdate = models.DateField(blank=True, null=True)
    
    is_admin = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """Return email."""
        return self.email