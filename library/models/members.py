from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

GENDER_CHOICES = [
    ('M', 'Man'),
    ('W', 'Woman')
]

ROLE_CHOICES = [
    ('S', 'Student'),
    ('T', 'Teacher'),
    ('O', 'Other')
]


class Member(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First Name')
    last_name = models.CharField(max_length=50, verbose_name='Last Name')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=20, verbose_name='Phone Number')
    birth_date = models.DateField(verbose_name='Date of Birth')
    age = models.IntegerField(validators=[MinValueValidator(6), MaxValueValidator(120)], verbose_name='Age')
    role = models.CharField(max_length=20, verbose_name='Role', choices=ROLE_CHOICES)
    active = models.BooleanField(default=True, verbose_name='Active')

    libraries = models.ManyToManyField('Library', related_name='members', verbose_name='Libraries')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
