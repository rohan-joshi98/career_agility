from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.conf import settings

CATEGORY_CHOICES=(
    ('people','PEOPLE'),
    ('brand','BRAND'),
    ('operation','OPERATION'),
    ('blank',' ')
)
PRIORITY_CHOICES=(
    ('high','HIGH'),
    ('modrate','MODRATE'),
    ('low','LOW'),
    ('blank',' ')
)
STATUS_CHOICES=(
    ('not_started,"NOT_STARTED'),
    ('in_progress','IN_PROGRESS'),
    ('completed','COMPLETED'),
    ('overschedule','OVERSCHEDULE'),
    ('blank',' ')
)
# Create your models here.
class Indicators(models.Model):
    indicators= models.CharField(max_length=225)
    page= models.CharField(max_length=50, default='landing')
    user= models.ForeignKey(User,on_delete=models.CASCADE)
