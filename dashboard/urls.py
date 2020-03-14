from django.conf.urls import url
from dashboard import views
from django.urls import path
from django.contrib import admin

urlpatterns = [

    path('home', views.home, name='home'),
    path('strategy', views.strategy, name='strategy'),
    path('brand', views.brand, name='brand'),
    path('operations', views.operations, name='operations'),
    path('people', views.people, name='people'),
    
]
