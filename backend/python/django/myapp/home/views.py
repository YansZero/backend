from django.shortcuts import render
from django.http import HttpResponse #import 需要的套件

# Create your views here.
def home(request):
    return HttpResponse("This is home page!") #回傳字串到前端