from django.shortcuts import render

# Create your views here.

def index(request):
    """
    A view to render the home screen
    """
    return render(request, 'home/index.html')