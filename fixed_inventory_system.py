"""Inventory management system for tracking stock items."""

import json
from datetime import datetime


class InventorySystem:
    """Manage inventory stock and operations."""

    def __init__(self):
        """Initialize the inventory system with empty stock."""
        self.stock_data = {}

    def add_item(self, item="default", qty=0, logs=None):
        """Add items to inventory and log the action."""
        if logs is None:
            logs = []
        if not item or not isinstance(item, str):
            return
        if not isinstance(qty, int):
            return
        self.stock_data[item] = self.stock_data.get(item, 0) + qty
        logs.append(
            f"{str(datetime.now())}: Added {qty} of {item}"
        )

    def remove_item(self, item, qty):
        """Remove items from inventory."""
        try:
            self.stock_data[item] -= qty
            if self.stock_data[item] <= 0:
                del self.stock_data[item]
        except KeyError:
            pass

    def get_qty(self, item):
        """Get quantity of an item in inventory."""
        return self.stock_data[item] if item in self.stock_data else 0

    def load_data(self, file="inventory.json"):
        """Load inventory data from a JSON file."""
        with open(file, "r", encoding="utf-8") as f:
            self.stock_data = json.load(f)

    def save_data(self, file="inventory.json"):
        """Save inventory data to a JSON file."""
        with open(file, "w", encoding="utf-8") as f:
            json.dump(self.stock_data, f)

    def print_data(self):
        """Print all items in inventory."""
        print("Items Report")
        for item, quantity in self.stock_data.items():
            print(f"{item} -> {quantity}")

    def check_low_items(self, threshold=5):
        """Return items with quantity below threshold."""
        result = []
        for item, quantity in self.stock_data.items():
            if quantity < threshold:
                result.append(item)
        return result


def main():
    """Main function to demonstrate inventory operations."""
    inventory = InventorySystem()
    inventory.add_item("apple", 10)
    inventory.add_item("banana", -2)
    inventory.remove_item("apple", 3)
    inventory.remove_item("orange", 1)
    print(f"Apple stock: {inventory.get_qty('apple')}")
    print(f"Low items: {inventory.check_low_items()}")
    inventory.save_data()
    inventory.load_data()
    inventory.print_data()


if __name__ == "__main__":
    main()
