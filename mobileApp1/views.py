from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    # Page from the theme
    return render(request, 'index.html')
# Create your views here.
