from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "frontpage"),
    path("todolist/", views.todolist, name = "todolist"),
]
