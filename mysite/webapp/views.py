from django.shortcuts import render
from django.http import HttpResponse

def index(reques):
    return HttpResponse("<h2>HEY!</h2>")
