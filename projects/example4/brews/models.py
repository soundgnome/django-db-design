# models.py - example4

from django.db import models


class AbstractRecipe(models.Model):
    name = models.CharField(max_length=255)
    directions = models.TextField()

    class Meta:
        abstract = True


class BaseRecipe(models.Model):
    pass


class Recipe(BaseRecipe, AbstractRecipe):
    pass


class Batch(BaseRecipe, AbstractRecipe):
    brew_date = models.DateField(blank=True, null=True)
    bottle_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)


class Ingredient(models.Model):
    recipe = models.ForeignKey('BaseRecipe', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    ingredient_type = models.CharField(max_length=255)
    amount = models.FloatField()
    measuerment_unit = models.CharField(max_length=255)
