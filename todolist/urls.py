from . import views
from django.urls import include, path

app_name = "todolist"
urlpatterns = [
    path("", views.index, name = "frontpage"),
    path("<str:username>/<str:board_name>", views.todo, name = "todo"),
]