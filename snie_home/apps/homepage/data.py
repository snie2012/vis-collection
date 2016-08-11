from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
import os
import json

dataPath = os.path.join(os.path.dirname(__file__), 'data/snie.json')

@csrf_protect
def serve_file(request):
    with open(dataPath, 'r', encoding='utf-8') as f:
        data = json.load(f, encoding='utf-8')
    return JsonResponse(data, safe=True)