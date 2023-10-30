from django.db import models

# Create your models here.

class Home_feild(models.Model):
    title = models.CharField(null=True, max_length=100)
    title2 = models.CharField(null=True, max_length=100)
    avatar = models.ImageField(null=True, default="avatar.svg")
    idea = models.CharField(max_length=200, null=True)
    details = models.TextField(max_length=500, null=True)
    
    def __str__(self):
        return self.title
