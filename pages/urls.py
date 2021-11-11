from django.urls import path
from .views import HomePageView, TestPageView, DataBasePageView
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('test/', TestPageView.as_view(), name='test'),
    path('data/', DataBasePageView.as_view(), name='data'),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]