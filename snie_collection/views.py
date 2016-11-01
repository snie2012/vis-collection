from django.shortcuts import render
from datetime import date
from django.utils.timezone import now

def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")