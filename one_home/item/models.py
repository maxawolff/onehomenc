"""Model for items to be purchased."""
from django.db import models


class Room(models.Model):
    """.Model for room of a house, will contain items."""

    name = models.CharField(max_length=50)


class Item(models.Model):
    """Model for item in store."""

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000,
                                   null=True,
                                   blank=True)
    # amount_needed = models.IntegerField()
    # amount_purchased = models.IntegerField()
    # use these if we want multiple of same item to be one model
    purchased = models.BooleanField(default=False)
    cost = models.FloatField()
    for_room = models.ForeignKey(Room,
                                 onDelete=models.Cascade,
                                 blank=True,
                                 null=True)
