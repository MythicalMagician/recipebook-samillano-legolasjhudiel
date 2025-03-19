# ledger/models.py
"""Classes for recipes and their ingredients."""

from django.db import models
from django.urls import reverse

from accounts.models import Profile


class Ingredient(models.Model):
    """
    Ingredient model.

    Has a name for the ingredient (100 characters max).
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        """Return name string."""
        return self.name


class Recipe(models.Model):
    """
    Recipe model.

    Each recipe instance has a name, author, and
    two dates for creation and most recent update.
    """

    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return name string."""
        return self.name

    def get_absolute_url(self):
        """Link to recipe page on admin interface."""
        return reverse('ledger:recipe_details', args=[self.pk])


class RecipeIngredient(models.Model):
    """
    RecipeIngredient model.

    Provides detail on amount of an ingredient
    to be used in a recipe.
    """

    quantity = models.CharField(max_length=100)

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipe'
    )

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients'
    )
