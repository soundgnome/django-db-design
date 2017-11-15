# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 02:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ingredient_type', models.CharField(max_length=255)),
                ('amount', models.FloatField()),
                ('measurement_unit', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('baserecipe_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='brews.BaseRecipe')),
                ('name', models.CharField(max_length=255)),
                ('directions', models.TextField()),
                ('brew_date', models.DateField(blank=True, null=True)),
                ('bottle_date', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('brews.baserecipe', models.Model),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('baserecipe_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='brews.BaseRecipe')),
                ('name', models.CharField(max_length=255)),
                ('directions', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('brews.baserecipe', models.Model),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brews.BaseRecipe'),
        ),
    ]
