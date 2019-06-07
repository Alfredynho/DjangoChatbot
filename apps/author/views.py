from django.shortcuts import render
from apps.author.models import Author
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class AuthorListView(ListView):
    model = Author
    template_name = "autores.html"
    context_object_name = "autores"


class AuthorDetailView(DetailView):
    model = Author
    template_name = "detalle_autor.html"
    context_object_name = "autor"
