# models.py - example2

from django.db import models


class AbstractRecipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    directions = models.TextField()

    class Meta:
        abstract = True


class Recipe(AbstractRecipe):
    pass


class Batch(AbstractRecipe):
    brew_date = models.DateField(blank=True, null=True)
    bottle_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)
