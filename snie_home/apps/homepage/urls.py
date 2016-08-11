from django.conf.urls import url
from django.shortcuts import render
from django.conf.urls import url, include
from . import views
from . import sections
from . import data

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
]

urlpatterns += [
    url(r'^snie_json/$', data.serve_file, name='file')
]

urlpatterns += [
    url(r'^poetry/', include('snie_home.apps.homepage.sections.poetry.urls', namespace="poetry")),
    url(r'^projects/', include('snie_home.apps.homepage.sections.projects.urls', namespace="projects")),
    url(r'^writings/', include('snie_home.apps.homepage.sections.writings.urls', namespace="writings"))
]