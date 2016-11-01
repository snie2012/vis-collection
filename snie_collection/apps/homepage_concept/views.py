from django.shortcuts import render

# moduleDir = os.path.dirname(__file__)  # get current directory

def homepage(request):
    return render(request, "homepage_concept/home.html")

