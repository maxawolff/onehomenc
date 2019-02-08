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


class RoomFactory(factory.django.DjangoModelFactory):
    """Factory for making a second buyer for testing."""

    class Meta:
        """Meta class."""

        model = Room

    name = 'Bedroom'


class ItemFactory(factory.django.DjangoModelFactory):
    """Factory for making an item for testing."""

    class Meta:
        """Meta class."""

        model = Item

    name = 'Sink'
    description = 'A sink, like to wash your hands with.'
    cost = 10.00


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


class RoomTestCase(TestCase):
    """Test case for Room model."""

    def setUp(self):
        """Set up room model to be tested."""
        self.room = RoomFactory.create()
        self.room.save()

    def test_room_exists(self):
        """Make sure room model is saved in database."""
        rooms = Room.objects.all()
        assert len(rooms) == 1

    def test_room_name_correct(self):
        """Make sure buyers first name is correct."""
        room = Room.objects.all()[0]
        assert room.name == 'Bedroom'


class ItemTestCase(TestCase):
    """Test case for Item model."""

    def setUp(self):
        """Set up item model to be tested."""
        self.item = ItemFactory.create()
        self.item.save()

    def test_item_exists(self):
        """Make sure item model is saved in database."""
        items = Item.objects.all()
        assert len(items) == 1

    def test_item_name_correct(self):
        """Make sure item name is correct."""
        item = Item.objects.all()[0]
        assert item.name == 'Sink'

    def test_item_description_correct(self):
        """Make sure item description is correct."""
        item = Item.objects.all()[0]
        assert item.description == 'A sink, like to wash your hands with.'

    def test_item_cost_correct(self):
        """Make sure item cost is correct."""
        item = Item.objects.all()[0]
        assert item.cost == 10.00

    def test_item_purchased_default_false(self):
        """Make sure an item's purchased attribute is false by default."""
        item = Item.objects.all()[0]
        assert item.purchased is False


# class ItemTestCase(TestCase):
#     """Tests for the item model."""

#     def test_test(self):
#         """A sample test."""
#         assert 1 == 1
