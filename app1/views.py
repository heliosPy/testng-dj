from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth.decorators import login_required
from .forms import StudentForm


def examin(request):
    return HttpResponse(
        "< h1 > R. Srinath Reddy < /h1 >"
    )


@login_required
def studentindex(request):
    print(request.session.get('_auth_user_id'))
    token = request.META.get('HTTP_AUTHORIZATION')
    session_id = request.META.get('HTTP_SESSION')
    print(session_id)
    # session = Session.objects.get(session_id=session_id)

    return HttpResponse('This is new view')


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        print(form)
        if form.is_valid():
            print(form.errors)
            return HttpResponse('hi')
    return render(request, 'add_student.html')
