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
    list_date = []
    k = Book.objects.order_by('pub_date').values('pub_date')
    for list in k:
        list_date.append(datetime.datetime.strftime(list['pub_date'], '%Y-%m-%d'))
    ind = list_date.index(pub_date)
    books = book.get(pub_date=pub_date)
    prev = 1
    next =1
    if ind == 0:
        prev = list_date[len(list_date)-1]
        next = list_date[ind + 1]
    elif ind == len(list_date)-1:
        prev = list_date[ind - 1]
        next = list_date[0]
    else:
        prev = list_date[ind-1]
        next = list_date[ind+1]

    return render(request, template, context = {
        'book': books,
        'prev': prev,
        'next': next
    })



