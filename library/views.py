from django.shortcuts import render, get_object_or_404
from .models import Book, Author, Genre


def home(request):
    books = Book.objects.select_related('author').prefetch_related('genre')
    genres = Genre.objects.all()

    genre_filter = request.GET.get('genre')
    if genre_filter:
        books = books.filter(genre__name=genre_filter)

    return render(request, 'library/home.html', {
        'books': books,
        'genres': genres,
        'selected_genre': genre_filter,
    })


def book_detail(request, pk):
    book = get_object_or_404(
        Book.objects.select_related('author').prefetch_related('genre'),
        pk=pk,
    )
    return render(request, 'library/book_detail.html', {'book': book})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = author.books.prefetch_related('genre')
    return render(request, 'library/author_detail.html', {
        'author': author,
        'books': books,
    })
