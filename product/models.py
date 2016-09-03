from django.db import models
# from section.models import Section
import json
# Create your models here.
from django.db.models import Sum
from transaction.models import TransactionDetails

class Timestampable(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=100)
    total_sale = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Product(Timestampable):
    barcode = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField()
    description = models.CharField(max_length=1000)

    # section = models.CharField(Section, related_name='product', on_delete=models.CASCADE)

    def get_rating(self):
        try:
            product_transact_details = TransactionDetails.objects.filter(product__id=self.id).aggregate(Sum('quantity'))
            category_quantity = Category.objects.get(id=self.category.id).total_sale
            total_quantity = product_transact_details['quantity__sum']

            if not total_quantity:
                total_quantity = 0
                rating = 0
            else:
                rating = (total_quantity /category_quantity) * 100
            return ("%.2f" % rating)
        except Exception as e:
            print(e)
            return 0

    def __str__(self):
        return self.name

