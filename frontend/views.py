from django.shortcuts import render

# Create your views here.


def index(request):
    """render the index page and react takes over from there"""
    return render(request, "frontend/index.html")
