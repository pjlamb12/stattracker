from django.db import models


class Player(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    number = models.CharField(max_length=2)
    def __unicode__(self):
        return self.number + ' ' + self.first_name + ' ' + self.last_name