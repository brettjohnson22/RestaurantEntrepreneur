from pizza import Pizza
from pasta import Pasta
from salad import Salad

class OrderFactory:

    @staticmethod
    def create_order(type):
        if type == 'pizza':
            return Pizza()
        elif type == 'pasta':
            return Pasta()
        elif type == 'salad':
            return Salad()
