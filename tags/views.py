from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from tags.models import Tag
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class TagListView(ListView):
    model = Tag
    template_name = "tags/list.html"
    paginate_by = 4


class TagDetailView(DetailView):
    model = Tag
    template_name = "tags/detail.html"


class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    template_name = "tags/new.html"
    fields = ["name", "recipes"]
    success_url = reverse_lazy("tags_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TagUpdateView(LoginRequiredMixin, UpdateView):
    model = Tag
    template_name = "tags/edit.html"
    fields = ["name", "recipes"]
    success_url = reverse_lazy("tags_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TagDeleteView(LoginRequiredMixin, DeleteView):
    model = Tag
    template_name = "tags/delete.html"
    success_url = reverse_lazy("tags_list")
