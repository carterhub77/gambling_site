from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)


class ItemInfo(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)

class Game(models.Model):
    status = models.CharField(max_length=100)  

class GamePlayer(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

class PlayerInventory(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)    
    itemInfo = models.ForeignKey(ItemInfo, on_delete=models.CASCADE)