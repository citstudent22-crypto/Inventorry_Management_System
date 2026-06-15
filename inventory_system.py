import csv
import os

FILE = "inventory.csv"


class InventorySystem:

    def __init__(self):
        if not os.path.exists(FILE):
            with open(FILE, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Product", "Price", "Quantity"])

    def add_product(self):
        pid = input("Product ID: ")
        name = input("Product Name: ")
        price = float(input("Price: "))
        qty = int(input("Quantity: "))

        with open(FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([pid, name, price, qty])

        print("Product Added Successfully!")

    def view_products(self):
        with open(FILE, "r") as f:
            reader = csv.reader(f)
            print("\n----- INVENTORY -----")
            for row in reader:
                print(row)

    def search_product(self):
        pid = input("Enter Product ID: ")

        with open(FILE, "r") as f:
            reader = csv.reader(f)

            for row in reader:
                if len(row) > 0 and row[0] == pid:
                    print("Product Found:", row)
                    return

        print("Product Not Found!")

    def update_stock(self):
        pid = input("Product ID: ")

        rows = []

        with open(FILE, "r") as f:
            reader = csv.reader(f)

            for row in reader:
                if len(row) > 0 and row[0] == pid:
                    row[3] = input("New Quantity: ")
                rows.append(row)

        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)

        print("Stock Updated!")

    def delete_product(self):
        pid = input("Product ID: ")

        rows = []

        with open(FILE, "r") as f:
            reader = csv.reader(f)

            for row in reader:
                if len(row) > 0 and row[0] != pid:
                    rows.append(row)

        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)

        print("Product Deleted!")

    def inventory_value(self):
        total = 0

        with open(FILE, "r") as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                total += float(row[2]) * int(row[3])

        print("\nTotal Inventory Value = Rs.", total)

    def menu(self):
        while True:
            print("\n===== INVENTORY SYSTEM =====")
            print("1. Add Product")
            print("2. View Products")
            print("3. Search Product")
            print("4. Update Stock")
            print("5. Delete Product")
            print("6. Inventory Value")
            print("7. Exit")

            choice = input("Enter Choice: ")

            if choice == "1":
                self.add_product()
            elif choice == "2":
                self.view_products()
            elif choice == "3":
                self.search_product()
            elif choice == "4":
                self.update_stock()
            elif choice == "5":
                self.delete_product()
            elif choice == "6":
                self.inventory_value()
            elif choice == "7":
                print("Exiting...")
                break
            else:
                print("Invalid Choice!")


system = InventorySystem()
system.menu()