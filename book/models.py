from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField()
    author = models.CharField(max_length=30, default='anonymous')
    email = models.EmailField(blank=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name
