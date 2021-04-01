from django.shortcuts import render


def homepage(request: object):
    return render(request, 'index.html')


def myhome(request: object):
    dict = {'name': 'SaiKrishna', 'Age': 33}
    return render(request, 'myhome.html', dict)
