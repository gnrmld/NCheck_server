from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import TransactionDetails


@receiver(post_save, sender=TransactionDetails)
def create_user_profile(sender, instance, created, **kwargs):
    print("HSKDFHSKJFHKSJHFKSJHFKSJDFHKSJFHKSJDFH")