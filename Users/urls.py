from Users import views
from django.urls import path

urlpatterns=[
    path('',views.HomeView.as_view(),name='index'),
    path('register/', views.register, name='register'),
    path('register_teacher/',views.register_teacher,name='register_teacher'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('list/', views.todolist, name='todolist'),
    path('update/<int:pk>/', views.update, name='update'),
    path('homework/',views.HomePage.as_view(),name='homework'),
    path("progress", views.progress, name="progress"),
    path('<slug:slug>/', views.DetailView.as_view(), name='task_detail'),
    path('<str:slug>/create/', views.TaskUpdateView.as_view(), name='task_create'),
]
