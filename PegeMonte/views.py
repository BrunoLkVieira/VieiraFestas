from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Tema

# Create your views here.

class Homepage(ListView):
    template_name = "homepage.html"
    model = Tema


class Detalhestema(DetailView):
    template_name = "detalhestema.html"
    model = Tema


class Pesquisa(ListView):
    template_name = "pesquisa.html"
    model = Tema


    def get_queryset(self):
        termo_pesquisa = self.request.GET.get("query")

        if termo_pesquisa:
            object_list = Tema.objects.filter(titulo__icontains= termo_pesquisa)
            return object_list
        else:
            return None
