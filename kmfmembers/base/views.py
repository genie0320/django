from django.shortcuts import render
from .models import Room

# Create your views here.

# rooms = [
#     {"id": 1, "name": "Lets learn python"},
#     {"id": 2, "name": "Lets learn javascript"},
#     {"id": 3, "name": "Lets learn discord"},
# ]


def index(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "base/index.html", context)


def room(request, pk):
    room_data = Room.objects.get(id=pk)
    context = {"room": room_data}
    return render(request, "base/room.html", context)
