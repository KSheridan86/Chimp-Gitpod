from django.urls import path
from . import views

urlpatterns = [
    # path('projects/', views.projects, name="projects"),
    path('', views.Home_Page, name="home-page"),
]
