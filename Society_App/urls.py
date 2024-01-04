from django.urls import include,path
from .views import *
urlpatterns = [
    path('', index, name= 'index'),
    path('login', login_view, name='login'),
    path('register',register_page, name='register'),
    path('admin',admin,name='admin'),
    path('Citizen',Citizen,name='Citizen'),
    path('Committee',Committee,name='Committee'),
    path('Security',Security,name='Security'),
]