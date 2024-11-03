from django.core.validators import MaxValueValidator
from django.db import models


GENRE_CHOICES = [
    ('Fiction', 'Fiction'),
    ('Non-Fiction', 'Non-Fiction'),
    ('Science Fiction', 'Science Fiction'),
    ('Fantasy', 'Fantasy'),
    ('Mystery', 'Mystery'),
    ('Horror', 'Horror'),
    ('Romance', 'Romance'),
    ('Thriller', 'Thriller'),
    ('Biography', 'Biography'),
    ('Autobiography', 'Autobiography'),
    ('Self-Help', 'Self-Help'),
    ('Cookbook', 'Cookbook'),
    ('Poetry', 'Poetry'),
    ('History', 'History'),
    ('Science', 'Science'),
    ('Art', 'Art'),
    ('Travel', 'Travel'),
    ('Children', 'Children'),
    ('Young Adult', 'Young Adult'),
    ('Other', 'Other'),
]


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    author_id = models.ForeignKey('Author', null=True, on_delete=models.SET_NULL, verbose_name='Author')
    publishing_date = models.DateField(verbose_name='Publishing Date')
    summary = models.TextField(null=True, blank=True, verbose_name='Summary')
    genre = models.CharField(max_length=50, null=True, choices=GENRE_CHOICES, verbose_name='Genre')
    page_count = models.IntegerField(null=True, verbose_name='Page Count')
    validators = [MaxValueValidator(10000)]

    publisher_id = models.ForeignKey('Publisher', null=True, on_delete=models.CASCADE, verbose_name='Publisher')