# ledger/views.py
"""Views displaying the homepage and recipes."""

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView

from .models import Recipe


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'
    context_object_name = 'recipes'


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'ledger/recipe_details.html'


class HomePageView(TemplateView):
    template_name = 'ledger/homepage.html'
