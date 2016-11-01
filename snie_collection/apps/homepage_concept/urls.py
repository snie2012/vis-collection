from django.conf.urls import url
from django.shortcuts import render
from django.conf.urls import url, include
from . import views
from . import data

# homwpage entry route
urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),

    # sample subpage
    url(r'^sample$', views.sample_subpage, name='sample_subpage'),

    # data access route
    url(r'^snie_json/$', data.serve_file, name='file'),

    # poem pages
    url(r'^jing_zhong/$', views.jing_zhong, name='jing_zhong'),
    url(r'^when_you_are_old/$', views.when_you_are_old, name='when_you_are_old'),
    url(r'^the_curse_of_adam/$', views.the_curse_of_adam, name='the_curse_of_adam')
]