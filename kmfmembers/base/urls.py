from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("room/<str:pk>/", views.room, name="room"),
    path("create_room/", views.createRoom, name="create-room"),
    path("update_room/<str:pk>", views.updateRoom, name="update-room"),
    path("delete/<str:pk>", views.deleteRoom, name="delete-room"),
    path("delete_comment/<str:pk>", views.deleteComment, name="delete-comment"),
    path("user_login/", views.userLogin, name="user-login"),
    path("user_join/", views.userJoin, name="user-join"),
    path("logout/", views.logoutUser, name="logout"),
]
