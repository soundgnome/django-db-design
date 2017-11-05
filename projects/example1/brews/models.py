# models.py

from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    directions = models.TextField()


class Batch(Recipe):
    brew_date = models.DateField(blank=True, null=True)
    bottle_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)
