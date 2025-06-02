# criar arquivo urls.py dentro da pasta website
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('produtos/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('localizacao/', views.localizacao, name='localizacao')
]
