from django.conf.urls import url
from django.shortcuts import render
from . import subpages

urlpatterns = [
    url(r'^jing_zhong/$', subpages.jing_zhong, name='jing_zhong'),
    url(r'^when_you_are_old/$', subpages.when_you_are_old, name='when_you_are_old'),
    url(r'^the_curse_of_adam/$', subpages.the_curse_of_adam, name='the_curse_of_adam')
]