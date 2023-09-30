from django.contrib import admin
from django.urls import path 
from Clean_Sight import views

urlpatterns =[
    path("",views.index,name='home')
]