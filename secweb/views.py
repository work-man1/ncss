from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    print('good to go')
    return render(request, 'index.html')