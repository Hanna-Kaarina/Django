from django.contrib import admin
from .models import Author, Genre, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'birth_date')
    search_fields = ('first_name', 'last_name')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'available')
    list_filter = ('available', 'genre', 'author')
    search_fields = ('title', 'isbn')
    filter_horizontal = ('genre',)
