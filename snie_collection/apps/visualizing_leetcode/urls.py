from django.conf.urls import url
from django.shortcuts import render
from django.conf.urls import url, include
from . import views

# homwpage entry route
urlpatterns = [
    url(r'^perfect_square/$', views.perfect_square, name='perfect_square'),
]