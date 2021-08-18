import unittest

from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink_1 = Drink("Bud Light", 3)

    def test_drink_has_name(self):
        self.assertEqual("Bud Light", self.drink_1.name)