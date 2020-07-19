from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Articles


class HomeListView(ListView):
    model = Articles
    template_name = 'base.html'
    context_object_name = 'list_articles'

class DetailPageListView(DetailView):
    model = Articles
    template_name = 'post_detail.html'
    context_object_name = 'get_article'