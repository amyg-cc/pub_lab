class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def add_money(self, money):
        self.till += money
