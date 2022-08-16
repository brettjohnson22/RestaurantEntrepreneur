from logger import logger
from order_factory import OrderFactory

class Franchise:
    def __init__(self, location_number):
        self.location_number = location_number

    def place_order(self):
        order = ''
        response = input(f"Welcome to The Original Beef of Chicagoland, location #{self.location_number}!\nWhat are you ordering?\nType '1' for pizza, '2' for pasta, '3' for salad.\n")

        if response == "1":
            order = OrderFactory.create_order('pizza')
        elif response == "2":
            order = OrderFactory.create_order('pasta')
        elif response == "3":
            order = OrderFactory.create_order('pizza')

        logger.log_transaction(order, self.location_number)
