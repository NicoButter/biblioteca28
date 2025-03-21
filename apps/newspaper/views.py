from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewspaperForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.db.models import Q, Count
from .models import Newspaper
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.utils.dateparse import parse_date


# -----------------------------------------------------------------------------------------------------------------------------

@login_required
def add_newspaper(request):
    if request.method == 'POST':
        print("Archivos recibidos:", request.FILES) 
        form = NewspaperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_dashboard')
        else:
            print("Errores del formulario:", form.errors)
    else:
        form = NewspaperForm()
    return render(request, 'newspaper/add_newspaper.html', {'form': form},  )

# -----------------------------------------------------------------------------------------------------------------------------

@method_decorator(login_required, name='dispatch')
class NewspaperSearchView(ListView):
    model = Newspaper
    template_name = 'newspaper/newspaper_search.html'
    context_object_name = 'newspapers'
    paginate_by = 10

    def get_queryset(self):
        # Recuperar los parámetros de la URL (GET)
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        query = self.request.GET.get('q')
        scope = self.request.GET.get('scope')
        genre = self.request.GET.get('genre')
        status = self.request.GET.get('status')

        queryset = super().get_queryset()
        queryset = queryset.annotate(cardex_count=Count('cardex_entries'))

        # Aplicar los filtros
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | 
                Q(publisher__icontains=query) |
                Q(description__icontains=query)
            )
        if scope:
            queryset = queryset.filter(scope=scope)
        if genre:
            queryset = queryset.filter(genre=genre)
        if status:
            queryset = queryset.filter(status=status)
        if start_date and end_date:
            start_date = parse_date(start_date)  # Parsear la fecha a un objeto de fecha
            end_date = parse_date(end_date)
            if start_date and end_date:
                queryset = queryset.filter(publication_date__range=[start_date, end_date])

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['scope'] = self.request.GET.get('scope', '')
        context['genre'] = self.request.GET.get('genre', '')
        context['status'] = self.request.GET.get('status', '')
        context['start_date'] = self.request.GET.get('start_date', '')
        context['end_date'] = self.request.GET.get('end_date', '')
        return context
    
# -----------------------------------------------------------------------------------------------------------------------------

@login_required
def newspaper_detail(request, pk):
    newspaper = get_object_or_404(Newspaper, pk=pk)
    
    return render(request, 'newspaper/newspaper_detail.html', {'newspaper': newspaper})

# ------------------------------------------------------------------------------------------------------------------------------

class NewspaperUpdateView(UpdateView):
    model = Newspaper
    fields = ['title', 'publisher', 'publication_date', 'scope', 'genre', 'status']
    template_name = 'newspaper/newspaper_update.html'