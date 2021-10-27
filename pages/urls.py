from django.urls import path
from .views import homePageView, testPageView, HomePageView, TestPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('test/', TestPageView.as_view(), name='test')
]