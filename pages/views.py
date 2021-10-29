from msilib.schema import ListView
from django.views.generic import TemplateView
from django.views.generic import ListView

from pages.models import Post


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
