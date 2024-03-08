from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-published_at']


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=10, null= True)
    
    def __str__(self):
        return self.first_name