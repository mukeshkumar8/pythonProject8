def add_vegetable(list):
    name = input("Enter vegetable name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    list[name] = {'quantity': quantity, 'price': price}

def remove_vegetable(list):
    name = input("Enter vegetable name to remove: ")
    if name in list:
        del list[name]
        print(f"{name} removed from inventory.")
    else:
        print(f"{name} not found in inventory.")

def view_inventory(list):
    print("Current list:")
    for name, details in list.items():
        print(f"Name: {name}, Quantity: {details['quantity']}, Price: {details['price']}")

list = {}
while True:
    print("1. Add Vegetable")
    print("2. Remove Vegetable")
    print("3. View Inventory")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_vegetable(list)
    elif choice == '2':
        remove_vegetable(list)
    elif choice == '3':
        view_inventory(list)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")