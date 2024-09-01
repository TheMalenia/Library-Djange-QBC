from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

# Create your views here.

# https://docs.djangoproject.com/en/5.1/topics/templates/ for template.
# Better : https://www.w3schools.com/django/django_templates.php


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def delete_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        book.delete()
        books = Book.objects.all()
        return render(request, 'delete_book.html', {'books': books, 'book': book})
    except:
        return redirect('book_list')

def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

def search_book(request):
    query = request.GET.get('q')
    books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    return render(request, 'book_list.html', {'books': books})

def filter_book(request):
    books = Book.objects.all()
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if min_price:
        books = books.filter(price__gte=min_price) # greater
    if max_price:
        books = books.filter(price__lte=max_price) # less
    if start_date:
        books = books.filter(publish_date__gte=start_date)
    if end_date:
        books = books.filter(publish_date__lte=end_date)

    return render(request, 'filtered_list.html', {'books': books})

def delete_filtered_books(request):
    books = Book.objects.all()
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if min_price:
        books = books.filter(price__gte=min_price) # greater
    if max_price:
        books = books.filter(price__lte=max_price) # less
    if start_date:
        books = books.filter(publish_date__gte=start_date)
    if end_date:
        books = books.filter(publish_date__lte=end_date)

    books.delete()
    return redirect('book_list')
    pass