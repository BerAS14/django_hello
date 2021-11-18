import json

from django.core.mail.backends import console
from django.views.generic import TemplateView
from django.views.generic import ListView
from rest_framework.response import Response
from rest_framework.views import APIView

from pages.models import Post

from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User

from .controller_game_snake import ControllerGameSnake
from .state_game_snake import StateGameSnake


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

def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__,
                      sort_keys=True, indent=4)


class GameSnake:
    controller = ControllerGameSnake()
    controller.game_init()
    jsonFile = toJSON(controller.state)


class StartPauseNewGameView(APIView):
    def get(self, request):
        GameSnake.controller.start_pause_new_game()
        # print(toJSON(GameSnake.controller.state))
        return Response(json.loads(toJSON(GameSnake.controller.state)))


class DoStepView(APIView):
    def get(self, request):
        GameSnake.controller.do_step()
        return Response(json.loads(toJSON(GameSnake.controller.state)))


class GoLeftView(APIView):
    def get(self, request):
        GameSnake.controller.go_left()
        return Response(json.loads(toJSON(GameSnake.controller.state.direction)))


class GoRightView(APIView):
    def get(self, request):
        GameSnake.controller.go_right()
        return Response(json.loads(toJSON(GameSnake.controller.state.direction)))


class GoUpView(APIView):
    def get(self, request):
        GameSnake.controller.go_up()
        return Response(json.loads(toJSON(GameSnake.controller.state.direction)))

class GoDownView(APIView):
    def get(self, request):
        GameSnake.controller.go_down()
        return Response(json.loads(toJSON(GameSnake.controller.state.direction)))

class GetStateView(APIView):
    def get(self, request):
        return Response(json.loads(toJSON(GameSnake.controller.state)))


# Create your views here.
