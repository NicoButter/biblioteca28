from django.contrib import admin
from .models import Cardex

@admin.register(Cardex)
class CardexAdmin(admin.ModelAdmin):
    list_display = ('newspaper', 'issue_number', 'circulation', 'created_at')
    search_fields = ('newspaper__title', 'issue_number')
    list_filter = ('created_at',)