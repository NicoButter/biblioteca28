from django.urls import path
from .views import add_newspaper, NewspaperSearchView, newspaper_detail

urlpatterns = [
    path('add/', add_newspaper, name='add_newspaper'),
    path('search/', NewspaperSearchView.as_view(), name='newspaper_search'),
    path('<int:pk>/', newspaper_detail, name='newspaper_detail'),

]
