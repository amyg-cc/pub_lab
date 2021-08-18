import unittest

from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Chanter", 800)
        self.drink_1 = Drink("vodka", 10)
        self.drink_2 = Drink("beer", 12)
        self.drinks =[self.drink_1, self.drink_2]
        self.customer_1 = Customer("Marcin", 100)

    def test_pub_has_name(self):
        self.assertEqual("The Chanter", self.pub.name)
        
    def test_add_money(self):
        self.pub.add_money(100)
        self.assertEqual(900, self.pub.till)

    def test_sell_drink(self):
        self.pub.sell_drink(self.drink_1, self.customer_1)
        self.assertEqual(90, self.customer_1.wallet)
        self.assertEqual(810, self.pub.till)