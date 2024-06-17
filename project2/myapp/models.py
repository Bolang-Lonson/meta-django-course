from django.db import models

# Create your models here.
class MenuItems(models.Model):
    itemName = models.CharField(max_length=200)
    category = models.CharField(max_length=300)
    year = models.IntegerField()