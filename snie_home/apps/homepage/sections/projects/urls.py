from django.conf.urls import url
from django.shortcuts import render
from . import views

urlpatterns = [
    url(r'^perfect_squares/$', views.perfect_squares, name='perfect_squares')
]