class CashRegister:
    def __init__(self, discount=0):
        # Validate discount via property setter
        self._discount = 0
        self.discount = discount  # triggers the setter
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
        """Add an item to the register."""
        self.total += price * quantity
        self.items.append(item)
        self.previous_transactions.append({
            "item": item,
            "price": price * quantity,
            "quantity": quantity
        })

    def apply_discount(self):
        """Apply the discount percentage to the total."""
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        discounted_total = self.total * ((100 - self.discount) / 100)
        self.total = discounted_total

        # Update last transaction to reflect discounted price
        last = self.previous_transactions[-1]
        last["price"] = last["price"] * ((100 - self.discount) / 100)
        self.items[-1] = self.items[-1]  # items list stays the same

        print(f"After the discount, the total comes to ${self.total:.2f}.")

    def void_last_transaction(self):
        """Remove the last transaction."""
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        last = self.previous_transactions.pop()
        self.total -= last["price"]
        self.items.pop()