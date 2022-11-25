from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def first(request):
    return HttpResponse('this is our first function')

def propose(request):
    return HttpResponse('<marquee>yes i love you</marquee>')

def rejection(request):
    return HttpResponse('<h2>frnd dialogue: Akka chellallu lera ra niku<h2>')
