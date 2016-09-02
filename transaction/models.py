from django.db import models
# from product.models import Timestampable
from shopper.models import Shopper
# Create your models here.


class Transaction(models.Model):
    shopper = models.ForeignKey(Shopper, related_name="transaction", on_delete=models.CASCADE)
    product = models.ManyToManyField('product.Product', related_name="transaction", through="TransactionDetails")
    total_price = models.IntegerField()
    payment_id = models.CharField(max_length=100)
    is_valid = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.payment_id


class TransactionDetails(models.Model):
    product = models.ForeignKey('product.Product', related_name="transaction_details")
    transaction = models.ForeignKey(Transaction)
    quantity = models.IntegerField(default=0)






