from django.shortcuts import render, redirect
from .forms import NewspaperForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.db.models import Q
from .models import Newspaper


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

# -----------------------------------------------------------------------------------------------------------------------------

@login_required
class NewspaperSearchView(ListView):
    model = Newspaper
    template_name = 'newspapers/newspaper_search.html'
    context_object_name = 'newspapers'
    paginate_by = 10  # Paginación opcional

    def get_queryset(self):
        query = self.request.GET.get('q')
        scope = self.request.GET.get('scope')
        genre = self.request.GET.get('genre')
        status = self.request.GET.get('status')

        # Consulta base
        queryset = super().get_queryset()

        # Filtros
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
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['scope'] = self.request.GET.get('scope', '')
        context['genre'] = self.request.GET.get('genre', '')
        context['status'] = self.request.GET.get('status', '')
        return context
    
# -----------------------------------------------------------------------------------------------------------------------------
