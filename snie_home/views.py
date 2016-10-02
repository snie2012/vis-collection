from django.shortcuts import render
from datetime import date
from django.utils.timezone import now

def home(request):
    today = date.today()
    return render(request, "home/index.html", {'today': today, 'now': now()})

def tmpRedirect(request):
    return render(request, "home/perfect-squares.html")

def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")