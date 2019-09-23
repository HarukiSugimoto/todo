from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('', views.home, name='home'),
    path('mypage/<str:username>/', views.mypage, name='mypage'),
    path('mypage/<str:username>/schedule/register', views.myschedule, name='schedule_register'),
    path('mypage/<str:username>/schedule/check', views.schedule_check, name='schedule_check'),
]