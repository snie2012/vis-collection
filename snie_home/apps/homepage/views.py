from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse

import os
import json

dataPath = os.path.join(os.path.dirname(__file__), 'static/homepage/data/snie.json')
# moduleDir = os.path.dirname(__file__)  # get current directory

def homepage(request):
    return render(request, "homepage/home.html")

@csrf_protect
def jsonFile(request):
    with open(dataPath, 'r') as f:
        data = json.load(f)
    return JsonResponse(data, safe=False)


def perfectSquares(request):
    return render(request, "d3/perfectSquares.html")

