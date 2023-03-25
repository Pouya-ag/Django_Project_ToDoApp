from django.urls import path,include
from . import views

urlpatterns = [
    #login
    path('login/', views.login_view, name='login'),
    # logout
    path('logout', views.logout_view, name='logout'),
    # register
    path('register/', views.register_view, name='register'),
    # api v1
    path('api/v1/', include('accounts.api.v1.urls'))
]