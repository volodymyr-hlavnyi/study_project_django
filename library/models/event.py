from datetime import timezone

from django.db import models

from library.models import Library, Book, Member


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='events')
    books = models.ManyToManyField(Book, related_name='events')


class EventParticipant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')
    member = models.ManyToManyField(Member, related_name='event_participations')
    registration_date = models.DateField(default=timezone.now)
