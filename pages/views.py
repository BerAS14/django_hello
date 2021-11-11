from django.views.generic import TemplateView
from django.views.generic import ListView


from pages.models import Post

from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


def homePageView(request):
    return HttpResponse('Hello, World!')


def testPageView(request):
    return HttpResponse('Hello, test!')


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class TestPageView(TemplateView):
    template_name = 'pages/test.html'


class DataBasePageView(ListView):
    model = Post
    template_name = 'pages/data.html'



# Create your views here.
