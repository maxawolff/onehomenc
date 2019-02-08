"""Model for items to be purchased."""
from django.db import models


class Buyer(models.Model):
    """.Model for room of a house, will contain items."""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    # purchases =


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
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True)
    purchased_by = models.ForeignKey(Buyer,
                                     on_delete=models.CASCADE,
                                     blank=True,
                                     null=True)
