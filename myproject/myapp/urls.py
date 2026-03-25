from . import views
from django.urls import path

urlpatterns = [
    path('', views.generate_paper, name="generate_paper"),
]
