from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book  # Се базира на моделот книга
        exclude = ("user",)  # user не се покажува во оваа форма, се друго да
