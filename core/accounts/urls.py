from django.urls import path
from . import views

urlpatterns = [
    #login
    path('login/', views.login_view, name='login'),
    # logout
    path('logout', views.logout_view, name='logout'),
    # register
    path('register/', views.register_view, name='register')
]