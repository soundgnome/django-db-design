# models.py - example5

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
    measurement_unit = models.CharField(max_length=255)


class Fermentable(Ingredient):

    def save(self, *args, **kwargs):
        self.ingredient_type = 'fermentable'
        self.measurement_unit = 'lbs'
        super(Fermentable, self).save(*args, **kwargs)

    class Meta:
        proxy = True



class Hop(Ingredient):

    def save(self, *args, **kwargs):
        self.ingredient_type = 'hop'
        self.measurement_unit = 'oz'
        super(Hop, self).save(*args, **kwargs)

    class Meta:
        proxy = True



class Yeast(Ingredient):

    def save(self, *args, **kwargs):
        self.ingredient_type = 'yeast'
        self.amount = 1
        self.measurement_unit = ''
        super(Yeast, self).save(*args, **kwargs)

    class Meta:
        proxy = True
