from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    """
    A view displaying list of all tasks only to logged-in users.    
    """
    model = Task
    template_name = "task_list.html"

    def get_queryset(self):
        """
        A function that filters tasks so that a user may see only user's tasks.
        """
        return Task.objects.filter(author=self.request.user)


class TaskDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """
    A view displaying one specific task only to logged-in user.
    """
    model = Task
    template_name = "task_detail.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A view to update a task. Only logged-in user may access.
    """
    model = Task
    fields = (
        "title",
        "priority",
        "due_date",
    )
    template_name = "task_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    A view to delete task. Only logged-in user may delete.
    """
    model = Task
    template_name = "task_delete.html"
    success_url = reverse_lazy("task_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class TaskCreateView(LoginRequiredMixin, CreateView):
    """
    A view to create new task. Only logged-in user may delete.
    """
    model = Task
    template_name = "task_new.html"
    fields = (
        "title",
        "due_date",
        "priority",
    )

    def form_valid(self, form):
        """
        Function that assigns currnet user as the author
        of the new task.
        """
        form.instance.author = self.request.user
        return super().form_valid(form) 
