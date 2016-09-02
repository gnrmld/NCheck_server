from django.db import models
from product.models import Timestampable, Product
from shopper.models import Shopper
# Create your models here.

class Transaction(Timestampable):
    shopper = models.ForeignKey(Shopper, related_name="transaction", on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, related_name="product")
    total_price = models.IntegerField()
    payment_id = models.CharField(max_length=100)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return self.payment_id



