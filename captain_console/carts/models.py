from django.db import models

# Create your models here.
from game.models import Game


class Cart(models.Model):
    game = models.ForeignKey(Game, null=True, blank=True)
    user = models.ForeignKey()
    console = models.ForeignKey()
    quantity = models.DecimalField()


    #def __unicode__(self):
    #    return "Cart id: %s" %(self.id)

    def __str__(self):
        return self.games.name
