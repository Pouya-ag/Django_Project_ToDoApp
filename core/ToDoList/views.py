from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from .models import Tasks
from .forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin


class TasksView(LoginRequiredMixin, CreateView, ListView):
    model = Tasks
    form_class = TaskForm
    context_object_name = 'all_tasks'
    success_url = '/ToDoList/tasks'

    def form_valid(self, form):
        form.instance.email = self.request.user
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        tasks = Tasks.objects.filter(email = self.request.user)
        return tasks

class DeleteView(DeleteView):
    model = Tasks
    success_url = '/ToDoList/tasks'

class EditView(UpdateView):
    model = Tasks
    form_class = TaskForm
    success_url = '/ToDoList/tasks'

class DoneView(UpdateView):
    model = Tasks
    fields = ['IsDone']
    success_url = '/ToDoList/tasks'