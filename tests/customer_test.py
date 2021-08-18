import unittest

from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer_1 = Customer("Peter", 100)

    def test_customer_has_name(self):
        self.assertEqual("Peter", self.customer_1.name)

    def test_customer_has_money(self):
        self.assertEqual(100, self.customer_1.wallet)

    def test_remove_money(self):
        self.customer_1.remove_money(50)
        self.assertEqual(50, self.customer_1.wallet)