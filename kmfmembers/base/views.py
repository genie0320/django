from django.shortcuts import render

# Create your views here.

rooms = [
    {"id": 1, "name": "Lets learn python"},
    {"id": 2, "name": "Lets learn javascript"},
    {"id": 3, "name": "Lets learn discord"},
]


def index(request):
    context = {"rooms": rooms}
    return render(request, "base/index.html", context)


def room(request, pk=None):
    if pk is None:
        return render(request, "base/room.html")
    room_data = None
    for data in rooms:
        if data["id"] == int(pk):
            room_data = data
    context = {"room": room_data}
    return render(request, "base/room.html", context)
