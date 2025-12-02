from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('academics/', views.academics, name='academics'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('admissions/', views.admissions, name='admissions'),
    path('fees/', views.fees, name='fees'),
]

