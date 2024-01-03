from django.shortcuts import render

def index(request):
    return render(request, "todolist/index.html")

def todolist(request):
    return render(request, "todolist/todo.html")