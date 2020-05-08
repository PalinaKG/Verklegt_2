from django.db import models

# Create your models here.
#<<<<<<< Updated upstream
from product.models import Product
#=======
#from game.models import Game
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes

#>>>>>>> Stashed changes


<<<<<<< Updated upstream
class Cart(models.Model):
    product=models.ManyToManyField(Product)
=======

#from product.models import Product
>>>>>>> Stashed changes

#<<<<<<< Updated upstream
    #game = models.ForeignKey(Product, on_delete=models.CASCADE)
    #user = models.ForeignKey(Product, on_delete=models.CASCADE)
    #console = models.ForeignKey(Product, on_delete=models.CASCADE)
    #quantity = models.DecimalField(Product, max_digits=10, decimal_places=2, default=0.0)
#=======

#from product.models import Product
#>>>>>>> Stashed changes

    def __str__(self):
        return self.product.name

    # def __unicode__(self):
    #    return "Cart id: %s" %(self.id)
