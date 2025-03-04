# ledger/admin.py
"""
Admin page.

Registers Ingredient, Recipe, and RecipeIngredient models.
Allows admins to manage the recipes in the admin dashboard.
"""
from django.contrib import admin

from .models import Ingredient, Recipe, RecipeIngredient


admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
