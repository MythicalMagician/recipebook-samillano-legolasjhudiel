# ledger/views.py
"""Views displaying the recipes."""

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from .models import Recipe


class RecipeListView(ListView):
    """View for recipe list."""

    model = Recipe
    template_name = 'ledger/recipe_list.html'
    context_object_name = 'recipes'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    """View for recipe. Requires login."""

    model = Recipe
    template_name = 'ledger/recipe_details.html'


def redirect_homepage(request):
    """Redirects to the recipe list from root URL."""
    return redirect('ledger:recipe_list')
