import unittest

from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer_1 = Customer("Peter", 100)

    def test_customer_has_name(self):
        self.assertEqual("Peter", self.customer_1.name)