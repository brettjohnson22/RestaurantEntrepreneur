from order import Order

class Pizza(Order):
    def __init__(self):
        super().__init__("Pizza", 15)

    def prepare(self):
        pass
