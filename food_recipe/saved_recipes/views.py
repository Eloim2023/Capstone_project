from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView
from .models import SavedRecipe
from recipes.models import Recipe

# Create your views here.


class SavedRecipeListView(LoginRequiredMixin, ListView):
    model = SavedRecipe
    template_name = 'saved_recipes/saved_recipe_list.html'
    context_object_name = 'saved_recipes'

    def get_queryset(self):
        return SavedRecipe.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        saved_recipes = context['saved_recipes']
        for saved_recipe in saved_recipes:
            recipe = saved_recipe.recipe
            if recipe is not None and recipe.ingredients:
                recipe.ingredients_list = recipe.ingredients.split('\n')
            else:
                recipe.ingredients_list = []

        return context


class SaveRecipeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        recipe_id = kwargs['recipe_id']
        try:
            recipe = Recipe.objects.get(id=recipe_id)

            print(recipe)
            recipe_clicked = SavedRecipe.objects.create(
                user=request.user, recipe=recipe)
            recipe_clicked.save()

            return redirect('saved_recipe_list')
        except Recipe.DoesNotExist:
            return redirect('home')