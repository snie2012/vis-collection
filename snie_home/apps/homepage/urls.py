from django.conf.urls import url
from django.shortcuts import render
from . import views

import os
import json

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^json/$', views.jsonFile, name='jsonFile'),
]

dataPath = os.path.join(os.path.dirname(__file__), 'static/homepage/data/snie.json')
subpages = {}

def constructRender(link):
    def requestHandler(request):
        return render(request, link)
    return requestHandler

def build(node):
    #url += [url(r'^(?P<string>[\w\-]+)$', views.jsonFile, name='jsonFile')]
    if 'src' in node:
        subpages[node['name']] = constructRender('homepage/subpages/' + node['src'])
    if 'children' in node:
        for c in node['children']:
            build(c)

with open(dataPath, 'r') as f:
    root = json.load(f)
    build(root)