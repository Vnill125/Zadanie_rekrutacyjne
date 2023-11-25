from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('task1/', views.task1, name='task1'),
    path('task2/', views.task2, name='task2')
]
