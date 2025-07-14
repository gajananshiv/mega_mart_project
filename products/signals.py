# products/signals.py

from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import ProductImage
import os

@receiver(post_delete, sender=ProductImage)
def delete_image_file(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Product, Category
from django.utils.text import slugify

@receiver(pre_save, sender=Product)
def generate_product_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)

@receiver(pre_save, sender=Category)
def generate_category_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product

@receiver(post_save, sender=Product)
def notify_product_created(sender, instance, created, **kwargs):
    if created:
        print(f"✅ New product created: {instance.name}")
    else:
        print(f"✏️ Product updated: {instance.name}")
