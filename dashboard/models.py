from django.db import models
from django import forms

CATEGORY_CHOICES=(
    ('people','PEOPLE'),
    ('brand','BRAND'),
    ('operation','OPERATION'),
    ('blank',' ')
)
# Create your models here.
class Indicators(models.Model):
    indicators= models.CharField(max_length=225)
    page= models.CharField(max_length=50, default='landing')
class Recommendation(models.Model):
    recommendations=models.TextField
    category=models.CharField(max_length=100,choices=CATEGORY_CHOICES, default=' ')
    