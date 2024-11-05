from django.db import models

class Library(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    location = models.CharField(max_length=200, verbose_name='Location')
    site = models.URLField(null=True, blank=True, verbose_name='Site URL')

    def __str__(self):
        return self.name
