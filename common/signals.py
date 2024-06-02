
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Product
from .elasticsearch import ProductDocument

@receiver(post_save, sender=Product)
def index_product(sender, instance, **kwargs):
    ProductDocument().update(instance)

@receiver(post_delete, sender=Product)
def delete_product(sender, instance, **kwargs):
    ProductDocument().delete(instance)
