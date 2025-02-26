from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'status', 'genre', 'physical_location')
    search_fields = ('title', 'authors', 'isbn')
    list_filter = ('status', 'genre', 'language')