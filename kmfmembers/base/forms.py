from django.forms import ModelForm
from .models import Room, Topic, Message

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' # db에 마련된 모든 필드를 반환함.