from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.urls import reverse
from .models import User, Board, Node
from .misc import getIP

# Create your views here.
def index(request):
    identity = getIP(request.META.get('HTTP_X_FORWARDED_FOR'), request.META.get('REMOTE_ADDR'))
    if request.method == "POST":
        data = request.POST
        if "username" in data:
            try:
                user = User.objects.get(username = data["username"])
                return render(request, "todolist/index.html", context = {"error_message": "User with this name already exists!"})
            except ObjectDoesNotExist:
                if not(data["username"]): 
                    return render(request, "todolist/index.html", context = {"error_message": "Invalid username!"})
                user = User(identity = identity, username = data["username"])
                user.save()
                return HttpResponseRedirect(reverse("todolist:frontpage"))
        if "board_name" in data:
            user = User.objects.get(identity = identity)
            try:
                board = Board.objects.get(name = data["board_name"], owner = user)
                return render(request, "todolist/index.html", context = {"error_message": "Board with this name already exists!", "user": user,})
            except ObjectDoesNotExist:
                if not(data["board_name"]): 
                    return render(request, "todolist/index.html", context = {"error_message": "Invalid board name!", "user": user,})
                board = Board(name = data["board_name"], owner = user)
                board.save()
                return HttpResponseRedirect(reverse("todolist:frontpage"))

    else:
        try:
            user = User.objects.get(identity = identity)
        except ObjectDoesNotExist:
            user = None
        return render(request, "todolist/index.html", context = {"user": user,}) 
        
def todo(request, username, board_name):
    identity = getIP(request.META.get('HTTP_X_FORWARDED_FOR'), request.META.get('REMOTE_ADDR'))
    if User.objects.get(username = username).identity != identity:
        return Http404()
    user = User.objects.get(identity = identity)
    board = Board.objects.get(name = board_name, owner = user)
    context = {
        "user": user,
        "board": board,
    }
    if request.method == "POST":
        data = request.POST

        for key in data:
            if key.split("_")[0] == "content":
                node = Node.objects.get(id = int(key.split("_")[1]), board = board)
                node.content = data[key]
                node.isdone = False
                node.save()
        for key in data:
            if key.split("_")[0] == "isdone":
                node = Node.objects.get(id = int(key.split("_")[1]), board = board)
                node.isdone = True
                node.save()

        if "exit" in data:    
            return HttpResponseRedirect(reverse("todolist:frontpage"))
        
        if "delete" in data:
            node = Node.objects.get(id = data["delete"], board = board)
            node.delete()
            return HttpResponseRedirect(reverse("todolist:todo", args = [username, board_name]))
        
        if data["new_content"] != "":
            node = Node(isdone = False, content = data["new_content"], board = board)
            node.save()
            
        return HttpResponseRedirect(reverse("todolist:todo", args = [username, board_name]))
    else:
        return render(request, "todolist/todo.html", context = context)
    