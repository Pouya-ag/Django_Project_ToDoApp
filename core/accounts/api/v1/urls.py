from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

app_name = "api-v1"

urlpatterns = [
    path('register/', views.RegisterApiView.as_view(), name="register"),
    path('change-password/', views.ChangePasswordView.as_view(), name="change-password"),
    path('login/', views.login_view, name="login"),
    path('jwt/create/',views.CustomTokenObtainPairView.as_view(),name='jwt-create'),
    path('jwt/refresh/',TokenRefreshView.as_view(),name='jwt-refresh'),
    path('jwt/verify/',TokenVerifyView.as_view(),name='jwt-verify'),

]