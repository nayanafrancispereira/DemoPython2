from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demoo(request):
 return HttpResponse("food is good")