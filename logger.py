from pizza import Pizza

class Logger():
    def __init__(self) -> None:
        self.transaction_count = 0
        self.daily_income = 0

    def log_transaction(self, order, store_number):
        self.transaction_count += 1
        self.daily_income += order.price
        file = open("log.txt", "a")
        file.write(f'TRX#{self.transaction_count}: {order.dish_name} at location {store_number} - ${order.price}. Total: ${self.daily_income}\n')
        file.close()

    def display_log(self):
        file = open("log.txt", "r")
        
logger = Logger()
