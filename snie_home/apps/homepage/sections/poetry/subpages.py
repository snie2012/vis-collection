from django.shortcuts import render

def jing_zhong(request):
    return render(request, "jing-zhong.html")

def when_you_are_old(request):
    return render(request, "when-you-are-old.html")

def the_curse_of_adam(request):
    return render(request, "the-curse-of-adam.html")