from django.urls import path
from . import views

app_name = "settings"

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:user_id>', views.user, name='user'),
    path('app/<app_id>', views.app, name='app'),
]