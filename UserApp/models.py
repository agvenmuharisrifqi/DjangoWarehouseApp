import imp
from django.db import models
from django.contrib.auth.models import User
from WarehouseApp.app_func import *
from datetime import timedelta, datetime
from PIL import Image
# Create your models here.

class BioUser(models.Model):
    custom_id = models.CharField(max_length=25, unique=True)
    image_profile = models.ImageField(upload_to='profile/', null=True, blank=True)
    # thumbnail_profile = models.ImageField()
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255)
    gender = models.CharField(max_length=2)
    address = models.CharField(max_length=255, null=True, blank=True)
    religion = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self):
        if not self.custom_id:
            self.custom_id = uniqueString(length=15)
            while BioUser.objects.filter(custom_id=self.custom_id).exists():
                self.custom_id = uniqueString(length=15)
        super(BioUser, self).save()

    def __str__(self):
        return self.id_number

    def get_position(self):
        return self.position

    def get_image_profile_url(self):
        return self.image_profile.url

    # def make_thumbnail(self, image, size=(40, 40)):
    #     img = Image.open(image)
    #     img.convert('RGB')


class SecretKey(models.Model):
    secret_key = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    add_secret = models.DateTimeField(auto_now=True)
    expiry_secret = models.DateTimeField(null=True, blank=True)
    
    def save(self):
        self.expiry_secret = datetime.now() + timedelta(days=1)
        super(SecretKey, self).save()

    def __str__(self):
        return self.user.username

