from email.policy import default
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from WarehouseApp.app_func import *

# Create your models here.
class Suplier(models.Model):
    custom_id = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=255, unique=True)
    suplier = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def save(self):
        if not self.custom_id:
            self.custom_id = uniqueString(length=15)
            while Suplier.objects.filter(custom_id=self.custom_id).exists():
                self.custom_id = uniqueString(length=15)
        super(Suplier, self).save()

    def __str__(self):
        return self.name

class Product(models.Model):
    custom_id = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255, unique=True)
    purchase = models.PositiveIntegerField()
    selling = models.PositiveIntegerField()
    stock = models.IntegerField(null=True, default=0)
    update = models.DateField(auto_now=True)
    descriptions = RichTextField(
        config_name='no_toolbar',
        null=True,
        blank=True,
    )
    company = models.ForeignKey(Suplier, on_delete=models.CASCADE)

    def save(self):
        if not self.custom_id:
            self.custom_id = uniqueString(length=15)
            while Product.objects.filter(custom_id=self.custom_id).exists():
                self.custom_id = uniqueString(length=15)
        super(Product, self).save()

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    custom_id = models.CharField(max_length=25, unique=True)
    status = models.BooleanField(null=True, blank=True)
    doc_type = models.CharField(max_length=3)
    number = models.CharField(max_length=255, unique=True)
    date = models.DateField()
    company = models.ForeignKey(Suplier, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    note = RichTextField(
        config_name='no_toolbar',
        null=True,
    )

    def save(self):
        if not self.custom_id:
            self.custom_id = uniqueString(length=15)
            while PurchaseOrder.objects.filter(custom_id=self.custom_id).exists():
                self.custom_id = uniqueString(length=15)
        super(PurchaseOrder, self).save()

    def __str__(self):
        return self.number

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    number = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)

    def save(self):
        super(Order, self).save()

    def __str__(self):
        return self.product.name
