from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("officer_history", views.officer_history, name="officer_history"),
]
