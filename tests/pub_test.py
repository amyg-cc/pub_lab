import unittest

from src.pub import Pub
# from src.customer import Customer

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Chanter", 800)
        self.drinks =[]

    def test_pub_has_name(self):
        self.assertEqual("The Chanter", self.pub.name)
        
    def test_add_money(self):
        self.pub.add_money(100)
        self.assertEqual(900, self.pub.till)