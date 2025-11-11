from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name = "index"),
    path("login", views.login, name = "login"),
    path("dashboard", views.dashboard, name = "dashboard"),
    path("QPMaker", views.QPMaker, name = "QPMaker")
]
