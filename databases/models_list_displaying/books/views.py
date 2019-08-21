from django.shortcuts import render
from .models import Book
import datetime
from django.core.paginator import Paginator

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.order_by('pub_date')
    context = {
        'books': books
    }
    return render(request, template, context)


def date_books(request, pub_date):
    template = 'books/book.html'
    book = Book.objects.order_by('pub_date')
    books = book.get(pub_date=pub_date)
    date = Book.objects.order_by('pub_date')
    date_next = date.filter(pub_date__gt=pub_date).first()
    if date_next == None:
        date_next = date.filter(pub_date__lt=pub_date).first()
    date_prev = date.filter(pub_date__lt=pub_date).last()
    if date_prev == None:
        date_prev = date.filter(pub_date__gt=pub_date).last()
    return render(request, template, context = {
        'book': books,
        'prev': date_prev.pub_date,
        'next': date_next.pub_date
    })



