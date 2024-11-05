from django.db import models

from library.models import Book, Member


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='reviews')
    rating = models.FloatField()
    description = models.TextField()
