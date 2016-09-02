from django.db import models

# Create your models here.


class Shopper(models.Model):
    shopper_id = models.IntegerField()
    name = models.CharField(max_length=100)
    address = models.TextField()
    points = models.IntegerField()

    def __str__(self):
        return self.name