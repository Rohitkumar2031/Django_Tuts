from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2> Hello Welcome my site hope you like it <h2>")

# Create your views here.
