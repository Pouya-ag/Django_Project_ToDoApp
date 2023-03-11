from django.contrib import admin
from .models import Tasks
from django.contrib.auth.admin import UserAdmin
from accounts.models import User

class ToDoList(UserAdmin):
    model = User
    list_display = (User, "Task")
    list_filter = (User,)
    search_fields = (User,)
    ordering = (User,)

admin.site.register(Tasks)