from . import views
from django.urls import path

from .views import LikeViews,CommentViews

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('<slug:slug>/', views.DetailView.as_view(), name='post_detail'),
    path('add_post',views.AddQueryview.as_view(),name='add_post'),
    path('update/<slug:slug>/',views.UpdateQueryView.as_view(),name='post_update'),
    path('delete/<slug:slug>/', views.DeleteQueryView.as_view(), name='post_delete'),
    path('like/<int:pk>',LikeViews,name='like_post'),
    path('comment/<int:pk>',views.CommentViews.as_view(),name='add_comment'),
    ]