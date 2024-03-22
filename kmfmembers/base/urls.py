from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("room/<str:pk>/", views.room, name="room"),
]
