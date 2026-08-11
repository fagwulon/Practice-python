class CardboardCup:
    def __init__(self, size, beverage, price, tax_rate=0.08):
        self.size = size
        self.beverage = beverage
        self.price = price
        self.tax_rate = tax_rate

    def __str__(self):
        """Prints a human-readable, clean receipt description."""  # This is a docstring
        # Calculate financial details
        tax_amount = self.price * self.tax_rate
        total_price = self.price + tax_amount

        # Build a beautiful, structured receipt layout
        receipt = (
            f"\n=========================="
            f"\n    DELIS COFFEE SHOP"
            f"\n=========================="
            f"\n Item: {self.size} {self.beverage}"
            f"\n Price: ${self.price: .2f}"
            f"\n Tax: ${tax_amount:.2f}"
            f"\n --------------------------"
            f"\n Total: ${total_price:.2f}\n"
        )
        return receipt


# --- Execution Example ---

# 1. Create a cup instance
cup = CardboardCup("Large", "Vanilla Latte", 4.58)

#  2. Print the cup directly to trigger __str__
print(cup)
