from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('employee/', views.employee_dashboard, name='employee_dashboard'),
    path('shift-leader/', views.shift_leader_dashboard, name='shift_leader_dashboard'),
]