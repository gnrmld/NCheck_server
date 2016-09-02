from django.db import models

# from section.models import Section

# Create your models here.

class Timestampable(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(Timestampable):
    barcode = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()
    # section = models.CharField(Section, related_name='product', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

