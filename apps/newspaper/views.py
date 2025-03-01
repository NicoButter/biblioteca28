from django.shortcuts import render, redirect
from .forms import NewspaperForm
from django.contrib.auth.decorators import login_required

@login_required
def add_newspaper(request):
    if request.method == 'POST':
        form = NewspaperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_dashboard')
    else:
        form = NewspaperForm()
    return render(request, 'newspaper/add_newspaper.html', {'form': form})