from django.db import models

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField('images/', null=True, blank=True)
    ingredients = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name