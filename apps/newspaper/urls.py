from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_newspaper, name='add_newspaper'),
    path('search/', views.NewspaperSearchView.as_view(), name='newspaper_search'),
    path('update/<int:pk>/', views.NewspaperUpdateView.as_view(), name='newspaper_update'),

]
