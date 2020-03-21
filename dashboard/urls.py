from django.conf.urls import url
from dashboard import views
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('home', views.home, name='home'),
    path('strategy', views.strategy, name='strategy'),
    path('brand', views.brand, name='brand'),
    path('operations', views.operations, name='operations'),
    path('people', views.people, name='people'),
    path('indicators', views.indicators, name='indicators'),
    path('indiform', views.indicators_form, name='indi_form'),
    path('tasks', views.indicators_form, name='indi_form'),
    path('recommform', views.recommendation_form, name='recom_form'),
]
