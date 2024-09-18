
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('test/', views.job_view_test2),
    path('add_job/', views.add_job)
]
