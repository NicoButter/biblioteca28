from django.shortcuts import render, redirect
from .forms import NewspaperForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.db.models import Q, Count
from .models import Newspaper
from django.utils.decorators import method_decorator

# -----------------------------------------------------------------------------------------------------------------------------

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

@method_decorator(login_required, name='dispatch')
class NewspaperSearchView(ListView):
    model = Newspaper
    template_name = 'newspaper/newspaper_search.html'
    context_object_name = 'newspapers'
    paginate_by = 10

    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        query = self.request.GET.get('q')
        scope = self.request.GET.get('scope')
        genre = self.request.GET.get('genre')
        status = self.request.GET.get('status')
        
        queryset = super().get_queryset()
        queryset = queryset.annotate(cardex_count=Count('cardex_entries'))
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
            queryset = queryset.filter(publication_date__range=[start_date, end_date])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['scope'] = self.request.GET.get('scope', '')
        context['genre'] = self.request.GET.get('genre', '')
        context['status'] = self.request.GET.get('status', '')
        return context
    
# -----------------------------------------------------------------------------------------------------------------------------
