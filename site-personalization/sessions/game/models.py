from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    # user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    name = models.TextField()


class Game(models.Model):
    membership = models.ManyToManyField(Player, through='PlayerGameInfo')
    number = models.IntegerField()
    status = models.BooleanField(default=False)

0
class PlayerGameInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    counter = models.IntegerField()
    author = models.BooleanField(default=False)

