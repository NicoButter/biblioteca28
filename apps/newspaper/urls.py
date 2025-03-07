from django.urls import path
from .views import add_newspaper, NewspaperSearchView

urlpatterns = [
    path('add/', add_newspaper, name='add_newspaper'),
    path('search/', NewspaperSearchView.as_view(), name='newspaper_search'),
]
