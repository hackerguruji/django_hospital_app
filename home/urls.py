from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("" , views.index, name='home'),
    path("dashboard", views.index, name='home'),
    path("consultation" , views.consultation, name='consultation'),
    path("report" , views.report, name='report'),   
]