"""Tests for the models."""
from django.test import TestCase
from .models import Buyer, Room, Item
import factory
import pdb


class BuyerFactory(factory.django.DjangoModelFactory):
    """Factory for making a buyer for testing."""

    class Meta:
        """Meta class."""

        model = Buyer

    first_name = 'Max'


# class BuyerFactory2(factory.django.DjangoModelFactory):
#     """Factory for making a second buyer for testing."""

#     class Meta:
#         """Meta class."""

#         model = Buyer

#     first_name = 'Bill'


class BuyerTestCase(TestCase):
    """Tests for the buyer model."""

    def setUp(self):
        """Set up user object for testing."""
        self.buyer = BuyerFactory.create()
        # self.buyer2 = BuyerFactory2.create()
        self.buyer.save()

    def test_buyer_exists(self):
        """Make sure buyer model is saved in database."""
        buyers = Buyer.objects.all()
        assert len(buyers) == 1
        # pdb.set_trace()


# class ItemTestCase(TestCase):
#     """Tests for the item model."""

#     def test_test(self):
#         """A sample test."""
#         assert 1 == 1
