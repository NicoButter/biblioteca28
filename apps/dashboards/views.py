from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    if request.user.rol != 'admin':
        return redirect('login')  
    return render(request, 'dashboard_app/admin_dashboard.html')

@login_required
def employee_dashboard(request):
    if request.user.rol != 'empleado':
        return redirect('login')
    return render(request, 'dashboard_app/employee_dashboard.html')

@login_required
def shift_leader_dashboard(request):
    if request.user.rol != 'jefe_turno':
        return redirect('login')
    return render(request, 'dashboard_app/shift_leader_dashboard.html')