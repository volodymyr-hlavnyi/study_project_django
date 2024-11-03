from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    address = models.CharField(max_length=256, null=True, verbose_name='Address')
    city = models.CharField(max_length=100, null=True, verbose_name='City')
    country = models.CharField(max_length=100, null=True, verbose_name='Country')