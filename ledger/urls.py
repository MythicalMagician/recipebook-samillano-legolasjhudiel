# ledger/urls.py
"""
Defines namespace, ledger, and matches views to corresponding URLs.

It displays parts of the recipe list based on recipe # for recipes 1 and 2.
"""

from django.urls import path
from .views import recipe_list, recipe_page

app_name = 'ledger'

urlpatterns = [
    path('recipes/list/', recipe_list, name="recipes"),
    path('recipe/1/', recipe_page, {'recipe_index': 0}, name="Recipe 1"),
    path('recipe/2/', recipe_page, {'recipe_index': 1}, name="Recipe 2")
]
