from django.urls import path
from . import views

app_name  = 'BlueVision_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('about/', views.about, name='about'),
    path('license/', views.license, name='license'),
    path('career/', views.career, name='career'),
]
