'''
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
'''
from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('read/<id>/', views.read),

    path('delete/', views.delete),
    path('update/<id>', views.update)
]

