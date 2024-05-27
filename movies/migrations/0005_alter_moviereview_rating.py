# Generated by Django 5.0.3 on 2024-05-26 01:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movie_budget_alter_movie_poster_path_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviereview',
            name='rating',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
