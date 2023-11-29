# myapp/urls.py
from django.urls import path
from .views import custom_login
from django.contrib import admin
from .views import custom_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('custom_login/', custom_login, name='custom_login'),
]