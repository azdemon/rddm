from django.shortcuts import render
from .models import Templates
from django.views.generic import TemplateView, ListView, DetailView


class IndexView(TemplateView):
    template_name = "certificates/index.html"
    

class CertListView(ListView):
    model = Templates
    template_name = "certificates/templates_list.html"
    context_object_name = 'templates'
    queryset = Templates.objects.all()
    

class CertDetailView(DetailView):
    model = Templates
    template_name = "certificates/templates_detail.html"
    context_object_name = 'template'
