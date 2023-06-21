from django.urls import path
from . import views

urlpatterns = [
    path ("", views.index),
    path ("brian/", views.brian, name = "brian"),
    path ("harry/", views.harry, name = "harry"),
    path ("greet/<str:name>", views.greet, name="greet"),


]