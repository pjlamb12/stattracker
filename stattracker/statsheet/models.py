from django.db import models
from player.models import Player


# Create your models here.
class Statsheet(models.Model):
    player = models.ForeignKey(Player, blank='true', null='true')
    game_day = models.DateTimeField('Game Date')
    offensive_rebounds = models.IntegerField(default=0)
    defensive_rebounds = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    steals = models.IntegerField(default=0)
    blocks = models.IntegerField(default=0)
    fouls = models.IntegerField(default=0)
    def __unicode__(self):
        return 'Statsheet ' + unicode(self.id) + ' for ' + self.player.first_name + ' ' + self.player.last_name + ' ' + unicode(self.game_day.month) + '/' + unicode(self.game_day.day) + '/' + unicode(self.game_day.year)