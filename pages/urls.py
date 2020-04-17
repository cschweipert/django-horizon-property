from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('alexa', views.alexa, name='alexa'),
    path('mls', views.mls, name='mls')
]