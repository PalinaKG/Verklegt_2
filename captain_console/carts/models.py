from django.db import models

# Create your models here.
from game.models import Game


class Cart(models.Model):
    games = models.ManyToManyField(Game, null=True, blank=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    #def __unicode__(self):
    #    return "Cart id: %s" %(self.id)

    def __str__(self):
        return self.games.name
