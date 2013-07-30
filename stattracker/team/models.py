from django.db import models
from player.models import Player


class Team(models.Model):
    players = models.ManyToManyField(Player, null='true', blank='true')
    team_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.team_name




