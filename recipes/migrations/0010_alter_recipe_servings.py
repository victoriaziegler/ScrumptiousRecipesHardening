# Generated by Django 4.0.3 on 2022-06-11 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_recipe_servings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='servings',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
