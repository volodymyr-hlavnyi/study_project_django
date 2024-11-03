from django.contrib import admin

from .models import Book, Author, Publisher


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Author._meta.fields]
    list_filter = ['deleted']
    search_fields = ['first_name', 'last_name', 'birth_date', 'deleted']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Book._meta.fields]
    list_filter = ['author_id']
    search_fields = ['title', 'author_id', 'publishing_date', 'genre', 'page_count']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Publisher._meta.fields]
    list_filter = []
    search_fields = []
