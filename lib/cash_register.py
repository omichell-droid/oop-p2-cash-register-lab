#!/usr/bin/env python3


class CashRegister:
    """A cash register for an e-commerce site."""

    def __init__(self, discount=0):
        self.discount = discount  # validated by the setter below
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # Discount is a whole-number percentage from 0 to 100
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        """Add an item (quantity times) and record the transaction."""
        self.total += price * quantity
        self.items.extend([item] * quantity)
        self.previous_transactions.append(
            {"item": item, "price": price, "quantity": quantity}
        )

    def apply_discount(self):
        """Take the discount percentage off the total."""
        if self.discount == 0 or not self.previous_transactions:
            print("There is no discount to apply.")
            return
        self.total = round(self.total * (100 - self.discount) / 100, 2)
        # Show 800 instead of 800.0 when the total is a whole number
        shown = int(self.total) if float(self.total).is_integer() else self.total
        print(f"After the discount, the total comes to ${shown}.")

    def void_last_transaction(self):
        """Undo the most recent add_item call."""
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return
        last = self.previous_transactions.pop()
        self.total = round(self.total - last["price"] * last["quantity"], 2)
        # Remove that transaction's items from the end of the list
        for _ in range(last["quantity"]):
            self.items.pop()
        if not self.previous_transactions:
            self.total = 0.0