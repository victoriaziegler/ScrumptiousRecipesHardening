from django.db import models
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL

# Create your models here.
# # Create meal plan model in the app
#     - Add fields to model
#         -model should have name, date, owner, and recipes fields


class MealPlans(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    # context_object_name = "meal_plans_list"
    owner = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE,
    )
    recipes = models.ManyToManyField("recipes.Recipe", related_name="recipes")
