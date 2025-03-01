from django.shortcuts import render, redirect
from .forms import BookForm
from django.contrib.auth.decorators import login_required  

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_dashboard')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})
