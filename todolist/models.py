from django.db import models

class User(models.Model):
    identity = models.CharField(max_length = 64)
    username = models.CharField(max_length = 30)
    def __str__(self):
        return self.username

class Board(models.Model):
    name = models.CharField(max_length = 50)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return f"name: {self.name} ; owner: {self. owner}"

class Node(models.Model):
    isdone = models.BooleanField()
    content = models.CharField(max_length = 300)
    board = models.ForeignKey(Board, on_delete = models.CASCADE)
    def __str__(self):
        return f"board: {self.board.__str__()} ; content: {self.content}"