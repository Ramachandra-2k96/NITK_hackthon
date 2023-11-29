# myapp/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import custom_login
from django.contrib import admin
from .views import custom_login,home,Custom_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('custom_login/', custom_login, name='custom_login'),
    path('home/', home, name='home'),
    path('logout/', Custom_logout, name='logout'),
]