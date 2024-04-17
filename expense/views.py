from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cost(request):
    return HttpResponse("Hello, Costly!")