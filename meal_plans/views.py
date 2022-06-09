# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from meal_plans.models import MealPlans
from django.contrib.auth.mixins import LoginRequiredMixin


# from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class MealPlansListView(LoginRequiredMixin, ListView):
    model = MealPlans
    template_name = "meal_plans/list.html"
    paginate_by = 6


class MealPlansDetailView(LoginRequiredMixin, DetailView):
    model = MealPlans
    template_name = "meal_plans/detail.html"


class MealPlansCreateView(LoginRequiredMixin, CreateView):
    model = MealPlans
    template_name = "meal_plans/create.html"
    fields = ["name", "recipes", "date"]
    success_url = reverse_lazy("meal_plans_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MealPlansUpdateView(LoginRequiredMixin, UpdateView):
    model = MealPlans
    template_name = "meal_plans/edit.html"
    fields = ["name", "date", "recipes"]
    success_url = reverse_lazy("meal_plans_list")


class MealPlansDeleteView(LoginRequiredMixin, DeleteView):
    model = MealPlans
    template_name = "meal_plans/delete.html"
    success_url = reverse_lazy("meal_plans_list")
