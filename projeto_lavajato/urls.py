from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('', views.homepage, name='homepage'),
]
