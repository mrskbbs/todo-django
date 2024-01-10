from hashlib import sha256
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import User, Board, Node
from .misc import getIP

# Create your views here.
def index(request):
    identity = sha256(getIP(request.META.get('HTTP_X_FORWARDED_FOR'), request.META.get('REMOTE_ADDR')).encode("utf-8")).hexdigest()
    if request.method == "POST":
        data = request.POST
        if "username" in data:
            user = User(identity = identity, username = data["username"])
            user.save()
        if "board_name" in data:
            user = User.objects.get(identity = identity)
            board = Board(name = data["board_name"], owner = user)
            board.save()     
        return HttpResponseRedirect("/")
    else:
        try:
            user = User.objects.get(identity = identity)
        except ObjectDoesNotExist:
            user = None
        return render(request, "todolist/index.html", context = {"user": user,}) 
        
def todo(request, username, board_name):
    identity = sha256(getIP(request.META.get('HTTP_X_FORWARDED_FOR'), request.META.get('REMOTE_ADDR')).encode("utf-8")).hexdigest()
    user = User.objects.get(identity = identity)
    board = Board.objects.get(name = board_name, owner = user)
    context = {
        "user": user,
        "board": board,
    }
    if request.method == "POST":
        data = request.POST
        print(data)
        if "new" in data:
            node = Node(isdone = False, content = data["content"], board = board)
            node.save()
        else:
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
                    
        return HttpResponseRedirect(f"/{username}/{board_name}")
    else:
        return render(request, "todolist/todo.html", context = context)
    