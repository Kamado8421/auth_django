from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('cad/', views.register, name='register'),
    #path('', views.plataforma, name='plataforma')
]