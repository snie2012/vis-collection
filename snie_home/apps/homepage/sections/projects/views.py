from django.shortcuts import render

# moduleDir = os.path.dirname(__file__)  # get current directory

def perfect_squares(request):
	return render(request, "perfect-squares.html")

