from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name  = 'BlueVisionWeb_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('send-message/', views.send_message, name='send_message'),
    path('show-data/', views.show_data, name='show_data'),
    path('service/', views.service, name='service'),
    path('about/', views.about, name='about'),
    path('license/', views.license, name='license'),
    path('career/', views.career, name='career'),
    #custom login, logout, register
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
]
