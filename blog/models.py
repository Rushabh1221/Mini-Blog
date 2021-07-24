from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    disc = models.TextField()    
    likes = models.ManyToManyField(User, related_name='like', default=None, blank=True)
    
    def number_of_likes(self):
        return self.likes.count()