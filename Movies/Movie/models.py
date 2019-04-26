from django.db import models

# Create your models here.
class movieType(models.Model):
    title=models.CharField(max_length=30)
    director=models.TextField()
    img=models.CharField(max_length=50)
    dec=models.TextField()
