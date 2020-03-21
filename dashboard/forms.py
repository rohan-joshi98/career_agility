from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from dashboard.models import Indicators
from django.db import models


ORGANIZATION_CHOICES=(
    ("exe","Example"),
    ("ca", "CareerAgility"),
)
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    organization = forms.ChoiceField(choices=ORGANIZATION_CHOICES)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class Indicators_Form(forms.ModelForm):
    indicators= forms.CharField(widget=forms.Textarea)
    page = forms.CharField()
    class Meta: 
        model= Indicators
        fields= ('indicators','page','user',)