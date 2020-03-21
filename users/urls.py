from django.conf.urls import url
from users import views as user_views
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name= "login/login.html"), name='login'),
    path('logout/', auth_views.LoginView.as_view(template_name="login/logout.html"), name='logout'),

]
