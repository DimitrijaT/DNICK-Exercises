from django.shortcuts import render
from .models import Book


# Create your views here.
def books(request):
    context = {"books": Book.objects.all(), "date": "09.05.2022"}
    return render(request, "books.html", context=context)
