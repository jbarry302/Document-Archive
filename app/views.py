from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Document
from .forms import DocumentForm

class IndexView(TemplateView):
    template_name = 'index.html'

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def terms_of_service(request):
    return render(request, 'terms_of_service.html')

class DocumentListView(ListView):
    model = Document
    template_name = 'document_list.html'
    context_object_name = 'documents'
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-created_at')
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )
        
        return queryset

class DocumentDetailView(DetailView):
    model = Document
    template_name = 'document_detail.html'

class DocumentCreateView(CreateView):
    model = Document
    form_class = DocumentForm
    template_name = 'document_create.html'
    success_url = reverse_lazy('app:documents')

class DocumentUpdateView(UpdateView):
    model = Document
    form_class = DocumentForm
    template_name = 'document_update.html'
    
    def get_success_url(self):
        return reverse_lazy('app:document_detail', kwargs={'pk': self.object.pk})

class DocumentDeleteView(DeleteView):
    model = Document
    success_url = reverse_lazy('app:documents')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)