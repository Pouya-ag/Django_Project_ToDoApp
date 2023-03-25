from django.urls import path
from . import views

app_name = "todolist-api-v1"

urlpatterns = [
    # path('list/', views.list_view, name="list"),
    # path('list/<int:pk>/', views.task_detail, name="task-detail"),
    path('list/', views.TaskList.as_view(), name="task-list"),
    path('list/<int:pk>/', views.TaskDetail.as_view(), name="task-detail"),
]