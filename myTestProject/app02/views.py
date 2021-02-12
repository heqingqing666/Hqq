from django.shortcuts import render,HttpResponse,redirect

# Create your views here.


def app02(request):
    return HttpResponse('app02的首页')