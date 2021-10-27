from django.http import HttpResponse
from django.views.generic import TemplateView


def homePageView(request):
    return HttpResponse('Hello, World!')
def testPageView(request):
    return HttpResponse('Hello, test!')

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class TestPageView(TemplateView):
    template_name = 'pages/test.html'

# Create your views here.
