from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "core/index.html")  # Adjust the path as needed
