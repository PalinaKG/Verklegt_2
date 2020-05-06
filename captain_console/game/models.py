from django.db import models
from console.models import Console


# Create your models here.
class GameGenre(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    price = models.FloatField()
    release_year = models.FloatField()
    developer = models.CharField(max_length=255)
    console = models.ForeignKey(Console, on_delete=models.CASCADE)
    genre = models.ForeignKey(GameGenre, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class GameImage(models.Model):
    image = models.CharField(max_length=999)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    def __str__(self):
        return self.image