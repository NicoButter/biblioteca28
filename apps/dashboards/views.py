from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    if request.user.rol != 'admin':
        return redirect('login')
    return render(request, 'dashboards/admin_dashboard.html', {
        'page_title': 'Tablero de Administrador',  # Aquí el título dinámico
    })

@login_required
def employee_dashboard(request):
    if request.user.rol != 'empleado':
        return redirect('login')
    return render(request, 'dashboards/employee_dashboard.html', {
        'page_title': 'Tablero de Trabajo',  # Aquí el título dinámico
    })

@login_required
def shift_leader_dashboard(request):
    if request.user.rol != 'jefe_turno':
        return redirect('login')
    return render(request, 'dashboards/shift_leader_dashboard.html', {
        'page_title': 'Tablero de Jefe de Turno',  # Aquí el título dinámico
    })
