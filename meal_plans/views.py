# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from meal_plans.models import MealPlans
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


# from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class MealPlansListView(LoginRequiredMixin, ListView):
    model = MealPlans
    template_name = "meal_plans/list.html"

    paginate_by = 6

    def get_queryset(self):
        return MealPlans.objects.filter(owner=self.request.user)


class MealPlansDetailView(LoginRequiredMixin, DetailView):
    model = MealPlans
    template_name = "meal_plans/detail.html"

    def get_queryset(self):
        return MealPlans.objects.filter(owner=self.request.user)


class MealPlansCreateView(LoginRequiredMixin, CreateView):
    model = MealPlans
    template_name = "meal_plans/create.html"
    fields = ["name", "recipes", "date"]
    success_url = reverse_lazy("meal_plans_list")

    def form_valid(self, form):
        plan = form.save(commit=False)
        plan.owner = self.request.user
        plan.save()
        form.save_m2m()
        return redirect("meal_plan_detail", pk=plan.id)


class MealPlansUpdateView(LoginRequiredMixin, UpdateView):
    model = MealPlans
    template_name = "meal_plans/edit.html"
    fields = ["name", "date", "recipes"]
    success_url = reverse_lazy("meal_plans_list")

    def get_queryset(self):
        return MealPlans.objects.filter(owner=self.request.user)


class MealPlansDeleteView(LoginRequiredMixin, DeleteView):
    model = MealPlans
    template_name = "meal_plans/delete.html"
    success_url = reverse_lazy("meal_plans_list")
