from django.urls import path
from . import views

urlpatterns = {
    path('exa/', views.examin, name='examin')
}