from email import message
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q

# from kmfmembers.base.views import userJoin
from .models import Room, Topic, Message
from .forms import RoomForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# rooms = [
#     {"id": 1, "name": "Lets learn python"},
#     {"id": 2, "name": "Lets learn javascript"},
#     {"id": 3, "name": "Lets learn discord"},
# ]


def index(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q)
    )
    comments = (
        Message.objects.all()
    )  # .order_by("-created") 아예 모델에서 이렇게 넘겨주게 해버렸음.
    topics = Topic.objects.all()
    room_count = rooms.count()

    context = {
        "rooms": rooms,
        "topics": topics,
        "room_count": room_count,
        "comments": comments,
    }
    return render(request, "base/index.html", context)


def room(request, pk):
    room_data = Room.objects.get(id=pk)
    comments = room_data.message_set.all().order_by("-created")
    members = room_data.members.all()

    if request.method == "POST":
        message = Message.objects.create(
            user=request.user,
            room=room_data,
            body=request.POST.get("body"),
        )
        # room_data.members.add(request.user) # 애당초... 가입도 안했는데, 댓글작성이 가능할리가...
        return redirect("room", pk=room_data.id)

    context = {"room": room_data, "comments": comments, "members": members}
    return render(request, "base/room.html", context)


@login_required(login_url="user-join")
def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {"form": form}
    return render(request, "base/room_form.html", context)


@login_required(login_url="user-join")
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse("작성자만 수정할 수 있다!")

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {"form": form}
    return render(request, "base/room_form.html", context)


@login_required(login_url="user-join")
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse("작성자만 수정할 수 있다!")

    if request.method == "POST":
        room.delete()
        return redirect("index")
    return render(request, "base/delete.html", {"obj": room})


def userLogin(request):
    page = "user-login"
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "아이디나 비밀번호를 확인해주세요.")

    context = {"page": page}
    return render(request, "base/user_login.html", context)


def userJoin(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            form.save()
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "뭔가 이상하다? 다시 확인해봐.")
    return render(request, "base/user_login.html", {"form": form})


def logoutUser(request):
    logout(request)
    return redirect("index")


@login_required(login_url="user-join")
def deleteComment(request, pk):
    comment = Message.objects.get(id=pk)

    if request.user != comment.user:
        return HttpResponse("작성자만 수정할 수 있다!")

    if request.method == "POST":
        comment.delete()
        return redirect("index")
    return render(request, "base/delete.html", {"obj": comment})
