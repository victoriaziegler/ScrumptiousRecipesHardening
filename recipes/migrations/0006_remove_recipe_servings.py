# Generated by Django 4.0.3 on 2022-06-11 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_recipe_servings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='servings',
        ),
    ]
