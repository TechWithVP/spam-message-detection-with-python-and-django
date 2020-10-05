from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "Index"),
    path('auth', views.index, name = "Index"),
    path('check', views.checkSpam, name = "CheckSpam"),
    path('logout', views.logout, name = "Logout"),
]
