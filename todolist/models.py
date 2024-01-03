from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 64)
    
    def __str__(self):
        return self.name

class Board(models.Model):
    name = models.CharField(max_length = 150)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    creation_date = models.DateTimeField()
    
    def __str__(self):
        return f"{self.name} ; {self.owner}"

class Node(models.Model):
    content = models.CharField(max_length = 200)
    is_done = models.BooleanField()
    board = models.ForeignKey(Board, on_delete = models.CASCADE)

    def __str__(self):
        return self.content