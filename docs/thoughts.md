## 장고프로젝트를 생성하는 두가지 방법

- 현재 폴더를 프로젝트 폴더로 설정하기
  django-admin startproject config .

- 현재폴더에 새로운 프로젝트폴더 생성하기
  django-admin startproject mysite

## 장고 앱을 생성하는방법

django-admin startapp pybo

## 동적경로 활용방법

views에서 이렇게 전달한 name은,
path("room/<str:pk>/", views.room, name="room"),

템플릿에서 아래와 같이 사용되는데...

<h5>{% url 'room' room.id %} -- {{ room.name }}</h5>
> 이름이 'room'인 데이터에서 id를 뽑아와라..는 뜻이고, 그 다음엔 그 뽑아온 걸 그대로 전달하는 모양.
앞에서 html명이 변경되더라도, 모든 페이지에서 경로를 변경하지 않아도 되는 것.
