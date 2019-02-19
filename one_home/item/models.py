"""Model for items to be purchased."""
from django.db import models


class Buyer(models.Model):
    """.Model for room of a house, will contain items."""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=500)

    def __str__(self):
        """Change how a buyer is displayed."""
        return (self.first_name + ' ' + self.last_name)
    # purchases =


class Room(models.Model):
    """.Model for room of a house, will contain items."""

    name = models.CharField(max_length=50)

    def __str__(self):
        """Change how a room is displayed."""
        return (self.name)


class Cart(models.Model):
    """Model for shopping cart."""

    purchaser = models.OneToOneField(Buyer, on_delete=models.CASCADE)


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
    in_cart = models.ForeignKey(Cart,
                                on_delete=models.SET_NULL,
                                blank=True,
                                null=True)

    def __str__(self):
        """Change how an item is displayed."""
        return (self.name)
