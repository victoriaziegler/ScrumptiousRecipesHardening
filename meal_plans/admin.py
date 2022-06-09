from django.contrib import admin

from meal_plans.models import MealPlans


# Register your models here.
class MealPlansAdmin(admin.ModelAdmin):
    pass


admin.site.register(MealPlans, MealPlansAdmin)
