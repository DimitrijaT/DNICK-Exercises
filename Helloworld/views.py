from django.shortcuts import render, redirect
from .models import Book
from datetime import datetime
from .forms import BookForm


# Create your views here.
def books(request):
    # POST REQUEST
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            # book.title = "TITLEFROMVIEW"
            book.save()
            return redirect("book")
    # user from the model == user from the client
    queryset = Book.objects.filter(user=request.user).all()
    context = {"books": queryset,
               "Date": datetime.now().date(),
               "form": BookForm}
    return render(request, "books.html", context=context)
