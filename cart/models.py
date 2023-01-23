from django.db import models
from shop.models import *


# Create your models here.
class cartlist(models.Model):
    objects = None
    cart_id = models.CharField(max_length=250, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.cart_id)


class items(models.Model):
    prodt = models.ForeignKey(products, on_delete=models.CASCADE)
    cart = models.ForeignKey(cartlist, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.prodt)

    def total(self):
        return self.prodt.price*self.quantity


