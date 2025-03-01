from django.contrib import admin
from .models import Newspaper

@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date', 'status')
    search_fields = ('title', 'publisher')
    list_filter = ('status', 'genre', 'language')