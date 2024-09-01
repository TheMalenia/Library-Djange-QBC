from django import forms
from .models import Book

# https://docs.djangoproject.com/en/5.1/topics/forms/modelforms/
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title',
                   'author',
                   'publish_date',
                   'price',
                   'description',
                   ]

# git friendly lol