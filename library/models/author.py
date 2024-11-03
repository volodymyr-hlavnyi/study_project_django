from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    birth_date = models.DateField(verbose_name='Birth Date')
    profile = models.URLField(null=True, blank=True, verbose_name='Profile URL')
    deleted = models.BooleanField(default=False, verbose_name='Deleted')
    rating = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ],
        verbose_name='Rating'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"