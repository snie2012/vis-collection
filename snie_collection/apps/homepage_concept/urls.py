from django.conf.urls import url
from django.shortcuts import render
from django.conf.urls import url, include
from . import views
from . import sections
from . import data

# homwpage entry route
urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
]

# data access route
urlpatterns += [
    url(r'^snie_json/$', data.serve_file, name='file')
]

# iframe access routes
urlpatterns += [
	#url(r'^home/', include('snie_collection.apps.homepage.sections.home.urls', namespace="writings")),
    url(r'^poetry/', include('snie_collection.apps.homepage_concept.sections.poetry.urls', namespace="poetry")),
    url(r'^projects/', include('snie_collection.apps.homepage_concept.sections.projects.urls', namespace="projects")),
    url(r'^writings/', include('snie_collection.apps.homepage_concept.sections.writings.urls', namespace="writings"))
]