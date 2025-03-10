from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CardexForm
from apps.newspaper.models import Newspaper

@login_required
def add_cardex(request, newspaper_id):
    newspaper = get_object_or_404(Newspaper, id=newspaper_id)
    if request.method == 'POST':
        form = CardexForm(request.POST)
        if form.is_valid():
            cardex = form.save(commit=False)
            cardex.newspaper = newspaper
            cardex.save()
            return redirect('newspaper_search')
    else:
        form = CardexForm()
    return render(request, 'cardex/add_cardex.html', {'form': form, 'newspaper': newspaper})