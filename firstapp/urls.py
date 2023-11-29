# myapp/urls.py
from django.urls import path
from .views import custom_login
from django.contrib import admin
from .views import custom_login,home,Custom_logout,meet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('custom_login/', custom_login, name='custom_login'),
    path('home/', home, name='home'),
    path('meet/', meet, name='meet'),
    path('logout/', Custom_logout, name='logout'),
]