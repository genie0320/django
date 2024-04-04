# Model에 손을 댔을 때는 언제나 python manage.py makemigrations > python manage.py migrate를 해 준다.

from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """Topic model"""

    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        """Return a string"""
        return self.name


# Create your models here.
class Room(models.Model):
    """Room model"""

    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    members = models.ManyToManyField(User, related_name="members", blank=True)
    updated = models.DateTimeField(auto_now=True)  # 호출될 때마다 업데이트 됨.
    created = models.DateTimeField(auto_now_add=True)  # '처음'에만 업데이트함.

    class Meta:
        ordering = [
            "-updated",
            "-created",
        ]  # - 를 붙이면 그 값을 기준으로 내림차순된다.

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE
    )  # 룸이 짤리면 메시지도 모두 삭제해라.
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [
            "-updated",
            "-created",
        ]  # - 를 붙이면 그 값을 기준으로 내림차순된다.

    def __str__(self):
        return self.body[0:50]
