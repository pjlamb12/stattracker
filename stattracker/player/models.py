from django.db import models
# from team.models import Team

class Player(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    number = models.CharField(max_length=2)
    # team = models.ForeignKey(Team)
    def __unicode__(self):
        return self.number + ' ' + self.first_name + ' ' + self.last_name