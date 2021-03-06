# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 23:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ingredients', models.TextField()),
                ('directions', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('recipe_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='brews.Recipe')),
                ('brew_date', models.DateField(blank=True, null=True)),
                ('bottle_date', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True)),
            ],
            bases=('brews.recipe',),
        ),
    ]
