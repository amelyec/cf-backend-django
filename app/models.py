from django.db import models
from django.forms import CharField

# Create your models here.
class Framework(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name +" "+ self.description