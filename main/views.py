from django.shortcuts import render, render
from django.http import HttpResponse

# Create your views here.
def home(response):
    return render(response, "main/final.html")