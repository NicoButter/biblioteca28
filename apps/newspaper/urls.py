from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_newspaper, name='add_newspaper'),
]
