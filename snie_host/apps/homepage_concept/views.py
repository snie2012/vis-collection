from django.shortcuts import render

# moduleDir = os.path.dirname(__file__)  # get current directory

def homepage(request):
    return render(request, "homepage_concept/home.html")

def sample_subpage(request):
    return render(request, "homepage_concept/sample_subpage.html")

def jing_zhong(request):
    return render(request, "homepage_concept/poetry/jing-zhong.html")

def when_you_are_old(request):
    return render(request, "homepage_concept/poetry/when-you-are-old.html")

def the_curse_of_adam(request):
    return render(request, "homepage_concept/poetry/the-curse-of-adam.html")
