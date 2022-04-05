from django.db import models

# Create your models here.
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