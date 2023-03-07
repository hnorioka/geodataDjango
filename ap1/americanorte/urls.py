from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("canada.html", views.canada, name="canada"),
    path("eua.html", views.eua, name="eua")
]