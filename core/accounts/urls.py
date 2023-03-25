from django.urls import path,include
from . import views
app_name = "accounts"

urlpatterns = [
    #login
    path('login/', views.login_view, name='login'),
    # logout
    path('logout', views.logout_view, name='logout'),
    # register
    path('register/', views.register_view, name='register'),
    # api v1
    path('api/v1/', include('accounts.api.v1.urls', namespace='ap-v1')),
    path('', include('django.contrib.auth.urls')),
]


# urlpatterns = [
#     path('api/v1/', include('accounts.api.v1.urls'))
# ]