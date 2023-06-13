from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def f3(req):
    return HttpResponse("<h1>hello from demo app2 using f3()</h1></hr>");
def f4(req):
    return HttpResponse("<h2>hello from demo app2 using f4()</h2></hr>");
