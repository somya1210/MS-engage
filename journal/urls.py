from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.index, name='h'),
    path('dashboard/add/', views.add, name='add')
]