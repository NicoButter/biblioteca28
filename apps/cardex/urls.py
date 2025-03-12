from django.urls import path
from . import views

urlpatterns = [
    path('newspaper/<int:newspaper_id>/cardex/add/', views.add_cardex, name='add_cardex'),
    path('add/<int:newspaper_id>/', views.add_cardex, name='add_cardex'),
]