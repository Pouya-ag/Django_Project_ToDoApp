from django.urls import path
from . import views

urlpatterns = [
    #tasks
    path('tasks/', views.TasksView.as_view(), name='tasks'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete-tesk'),
    path('edit/<int:pk>/', views.EditView.as_view(), name='edit-tesk'),
    path('done/<int:pk>/', views.DoneView.as_view(), name='done-tesk'),
]