from django.shortcuts import render


def homepage(request: object):
    return render(request, 'index.html')
