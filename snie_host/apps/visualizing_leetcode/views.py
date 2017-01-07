from django.shortcuts import render

# moduleDir = os.path.dirname(__file__)  # get current directory

def perfect_square(request):
    return render(request, "visualizing_leetcode/perfect_squares.html")

