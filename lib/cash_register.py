class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if not isinstance(value, int):
            print("Not valid discount")
            return
        if not (0 <= value <= 100):
            print("Not valid discount")
            return
        self._discount = value

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        # Add item once per quantity
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append({
            "item": item,
            "price": price * quantity,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total = self.total * ((100 - self.discount) / 100)

        # Format: strip trailing zeros e.g. $800. not $800.00
        formatted = f"${self.total:g}"
        # But keep 2 decimal places if there are cents
        if '.' not in formatted:
            formatted = formatted  # whole number, no decimals needed
        
        print(f"After the discount, the total comes to {formatted}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        last = self.previous_transactions.pop()
        self.total -= last["price"]
        # Remove quantity number of items
        for _ in range(last["quantity"]):
            self.items.pop()