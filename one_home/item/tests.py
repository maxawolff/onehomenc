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
    last_name = 'Wolff'
    address = '2901 Oakley Woods Lane, Apex NC, 27539'


class BuyerFactory2(factory.django.DjangoModelFactory):
    """Factory for making a second buyer for testing."""

    class Meta:
        """Meta class."""

        model = Buyer

    first_name = 'Bill'


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

    def test_buyer_first_name_correct(self):
        """Make sure buyers first name is correct."""
        buyer = Buyer.objects.all()[0]
        assert buyer.first_name == 'Max'

    def test_buyer_last_name_correct(self):
        """Make sure buyers last name is correct."""
        buyer = Buyer.objects.all()[0]
        assert buyer.last_name == 'Wolff'

    def test_buyer_address_correct(self):
        """Make sure buyers address is correct."""
        buyer = Buyer.objects.all()[0]
        assert buyer.address == '2901 Oakley Woods Lane, Apex NC, 27539'

    def tearDown(self):
        """Delete the buyer object after it is used."""
        Buyer.objects.all()[0].delete()


# class ItemTestCase(TestCase):
#     """Tests for the item model."""

#     def test_test(self):
#         """A sample test."""
#         assert 1 == 1
