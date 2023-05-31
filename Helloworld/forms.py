from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = 'form-control'

    class Meta:
        model = Book  # Се базира на моделот книга
        exclude = ("user",)  # user не се покажува во оваа форма, се друго да


