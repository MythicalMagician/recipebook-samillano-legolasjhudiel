# ledger/urls.py
from django.urls import path
from .views import recipe_list, recipe_page

app_name = 'ledger'

urlpatterns = [
    path('recipes/list/', recipe_list, name="recipes"),
    path('recipe/1/', recipe_page, {'recipe_index': 0}, name="Recipe 1"),
    path('recipe/2/', recipe_page, {'recipe_index': 1}, name="Recipe 2")
]