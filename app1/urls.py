from django.urls import path
from . import views

urlpatterns = [
    path('exa/', views.examin, name='examin'),
    path('index/', views.studentindex, name='index'),
    path('add/', views.add_student, name='add'),
]
