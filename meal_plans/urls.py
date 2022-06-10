from django.urls import path

from meal_plans.views import (
    MealPlansListView,
    MealPlansDetailView,
    MealPlansCreateView,
    MealPlansUpdateView,
    MealPlansDeleteView,
)


urlpatterns = [
    path("", MealPlansListView.as_view(), name="meal_plans_list"),
    path("<int:pk>/", MealPlansDetailView.as_view(), name="meal_plans_detail"),
    path(
        "<int:pk>/delete/",
        MealPlansDeleteView.as_view(),
        name="meal_plans_delete",
    ),
    path("create/", MealPlansCreateView.as_view(), name="meal_plans_create"),
    path(
        "int:pk>/edit/", MealPlansUpdateView.as_view(), name="meal_plans_edit"
    ),
]
