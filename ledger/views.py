# ledger/views.py
"""Returns views of the homepage, recipe list, and recipe pages."""

from django.shortcuts import render

context = {
    "recipes": [
        {
            "name": "Recipe 1",
            "ingredients": [
                {
                    "name": "tomato",
                    "quantity": "3pcs"
                },
                {
                    "name": "onion",
                    "quantity": "1pc"
                },
                {
                    "name": "pork",
                    "quantity": "1kg"
                },
                {
                    "name": "water",
                    "quantity": "1L"
                },
                {
                    "name": "sinigang mix",
                    "quantity": "1 packet"
                }
            ],
            "link": "/recipe/1"
        },
        {
            "name": "Recipe 2",
            "ingredients": [
                {
                    "name": "garlic",
                    "quantity": "1 head"
                },
                {
                    "name": "onion",
                    "quantity": "1pc"
                },
                {
                    "name": "vinegar",
                    "quantity": "1/2cup"
                },
                {
                    "name": "water",
                    "quantity": "1 cup"
                },
                {
                    "name": "salt",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "whole black peppers",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "pork",
                    "quantity": "1 kilo"
                }
            ],
            "link": "/recipe/2"
        }
    ]
}


def recipe_list(request):
    """Return a view of the names of recipes in the recipe list."""
    recipes = context
    return render(request, 'ledger/recipe_list.html', {'recipes': recipes})


def recipe_page(request, recipe_index):
    """Return a view displaying the content of a recipe from the list."""
    recipe = context["recipes"][recipe_index]
    return render(request, 'ledger/recipe_details.html', {'recipe': recipe})


def ledger_homepage(request):
    """Return a view of the homepage."""
    return render(request, 'ledger/homepage.html')
