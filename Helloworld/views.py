from django.shortcuts import render
from .models import Book
from datetime import datetime
from .forms import BookForm


# Create your views here.
def books(request):
    # user from the model == user from the client
    queryset = Book.objects.filter(user=request.user).all()
    context = {"books": queryset,
               "Date": datetime.now().date(),
               "form": BookForm}
    return render(request, "books.html", context=context)
