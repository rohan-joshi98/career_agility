from django.db import models

# Create your models here.
class Indicators(models.Model):
    indicators= models.CharField(max_length=225)