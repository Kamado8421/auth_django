from django.contrib import admin
from django.urls import path, include
from login_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('login_app.urls')),
    path('', views.plataforma, name="plataforma")
]
