from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, wasxcxdasorld. You're at the polls index.")