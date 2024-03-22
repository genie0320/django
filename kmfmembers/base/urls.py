from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("room/", views.room, name="room"),
    path("room/<str:pk>/", views.room, name="room"),
]
