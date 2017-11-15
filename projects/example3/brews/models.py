# models.py - example3

from django.db import models


class AbstractRecipe(models.Model):
    name = models.CharField(max_length=255)
    directions = models.TextField()

    class Meta:
        abstract = True


class Recipe(AbstractRecipe):
    pass


class Batch(AbstractRecipe):
    brew_date = models.DateField(blank=True, null=True)
    bottle_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)


class Ingredient(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    ingredient_type = models.CharField(max_length=255)
    amount = models.FloatField()
    measurement_unit = models.CharField(max_length=255)
