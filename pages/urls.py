from django.urls import path
from .views import homePageView, testPageView, HomePageView, TestPageView, DataBasePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('test/', TestPageView.as_view(), name='test'),
    path('data/', DataBasePageView.as_view(), name='data')
]