from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def examin(request):
    return HttpResponse(
        "< h1 > R. Srinath Reddy < /h1 >"
    )


def studentindex(request):
    return HttpResponse('This is new view')
