from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def f1(req):
    return HttpResponse("<h1> ****Hello from demo app1 using f1()****</h1><hr/>");
def f2(req):
    return HttpResponse("<h2> hello user56 from demo app2 using f2()</h2><hr />");
