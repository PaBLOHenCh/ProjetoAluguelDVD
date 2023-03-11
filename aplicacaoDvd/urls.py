from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('dvds/', include('dvds.urls')),
    path('accounts/', include('clientes.urls')),
    
]
