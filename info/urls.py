from django.contrib import admin
from django.urls import path
from info import views

urlpatterns = [
    path('', views.index, name="home"),
    path('projects', views.project, name="projects"),
    path('qualification', views.qualification, name="qualification")
]