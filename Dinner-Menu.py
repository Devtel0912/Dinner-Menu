class Greeting:
    def display(self):
        print("=" * 50)
        print("✨ Welcome to Dev's Dinner Menu ✨".center(50))
        print("=" * 50)

class Dinner:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Drinks:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Appetizer:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Dessert:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:

    def __init__(self):
        
        self.items = []

    def add(self, item):

        self.items.append(item)

        print(f"Added {item.name} to you order!")

    def total(self):

        return sum(item.price for item in self.items)
    
    def show_order(self):

        if not self.items:

            print(" There are 0 items")

            return
        
        print(" Here's Your Order:")

        for i, item in enumerate(self.items,1):

            print(f"{i}. {item.name} - ${item.price}")

        print(f"Total: ${self.total()}\n")


    def checkout(self):

            if not self.items:

                print("Empty")

                return
            self.show_order()

            confirm = input("Proceed to check out? (y/n)").strip().lower()

            if confirm == "y":

                print("ORDER CONFIRMED")
            
                self.items.clear()

            else:

                print("Checkout Cancelled")



def main():
    drinks_menu = [

        Drinks("Wine",50),

        Drinks("Champagne",100),

        Drinks("Soft Drinks",5),

        Drinks("Water",1)
    ]

    
    appetizer_menu = [
        Appetizer("Garlic Bread", 8),
        Appetizer("Bruschetta", 10),
        Appetizer("Fries", 5)
    ]




    Dinner_menu = [
        Dinner("Fettuchi Alfredo",20),

        Dinner("Mac And Cheese",15),

        Dinner("Chicken Burger or Veggie Burger",15),

        Dinner("Fish n Chips", 20),

        Dinner("Grilled Salmon",20)
    ]


    Dessert_Menu = [
        Dessert("Lava Cake",20),
        Dessert("Cheesecake",20),
        Dessert("Ice Cream",5)
    ]

    order = Order()
    stage = 'drinks'

    while True:

        if stage == "drinks":
            print("\n------ Drinks Menu ------")
            for i, item in enumerate(drinks_menu, 1):
                print(f"{i}. {item.name} - ${item.price}")

            choice = input("Choose a drink: ")

            if choice.isdigit() and 1 <= int(choice) <= len(drinks_menu):
                order.add(drinks_menu[int(choice) - 1])
                stage = "appetizers"   # AUTO MOVE
            else:
                print("Invalid choice.")

        elif stage == "appetizers":
            print("\n------ Appetizer Menu ------")
            for i, item in enumerate(appetizer_menu, 1):
                print(f"{i}. {item.name} - ${item.price}")

            choice = input("Choose an appetizer: ")

            if choice.isdigit() and 1 <= int(choice) <= len(appetizer_menu):
                order.add(appetizer_menu[int(choice) - 1])
                stage = "dinner"      # AUTO MOVE
            else:
                print("Invalid choice.")

        elif stage == "dinner":
            print("\n------ Dinner Menu ------")
            for i, item in enumerate(Dinner_menu, 1):
                print(f"{i}. {item.name} - ${item.price}")

            choice = input("Choose a dinner item: ")

            if choice.isdigit() and 1 <= int(choice) <= len(Dinner_menu):
                order.add(Dinner_menu[int(choice) - 1])
                stage = "dessert"     # AUTO MOVE
            else:
                print("Invalid choice.")

        elif stage == "dessert":
            print("\n------ Dessert Menu ------")
            for i, item in enumerate(Dessert_Menu, 1):
                print(f"{i}. {item.name} - ${item.price}")

            print(f"{len(Dessert_Menu) + 1}. Skip Dessert")

            choice = input("Choose a dessert or skip: ")

            if choice.isdigit() and 1 <= int(choice) <= len(Dessert_Menu):
                order.add(Dessert_Menu[int(choice) - 1])
                stage = "actions"
            elif choice == str(len(Dessert_Menu) + 1):
                 stage = "actions"
            else:
                print("Invalid choice.")

#-----------Actions---------------------------

        elif stage == "actions":
            print("\n------ Order Actions ------")
            print("1. View Order")
            print("2. Checkout")
            print("3. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                order.show_order()
            elif choice == "2":
                order.checkout()
                stage = "drinks"   # restart flow after checkout
            elif choice == "3":
                print("Goodbye 👋")
                break
            else:
                print("Invalid choice.")




if __name__ == "__main__":
    greeting = Greeting()
    greeting.display()
    main()

