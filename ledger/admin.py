# ledger/admin.py
"""
Admin page.

Registers Ingredient, Recipe, and RecipeIngredient models.
Allows admins to manage the recipes in the admin dashboard.
"""

from django.contrib import admin

from .models import Ingredient, Recipe, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    """Inline for editing RecipeIngredient instances."""

    model = RecipeIngredient


class IngredientAdmin(admin.ModelAdmin):
    """
    Admin interface for Ingredient.

    Allows searching by name.
    Displays names in the list.
    """

    model = Ingredient
    search_fields = ('name',)
    list_display = ('name',)


class RecipeAdmin(admin.ModelAdmin):
    """
    Admin interface for Recipe.

    Allows searching by name.
    Displays names in the list.
    Allows for configuring its ingredients.
    """

    model = Recipe
    search_fields = ('name',)
    list_display = ('name',)
    inlines = [RecipeIngredientInline]


class RecipeIngredientAdmin(admin.ModelAdmin):
    """
    Admin interface for RecipeIngredient.

    Lists individual ingredients, their quantities,
    and their related recipes.
    """

    model = RecipeIngredient
    list_display = ('recipe', 'ingredient', 'quantity')


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
