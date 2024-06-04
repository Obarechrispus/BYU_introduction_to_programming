"""
Author: Chrispas Obare Moraa
A simple shopping cart program for a shopping list
"""
price_list = []
shopping_cart = []

while True:
    try:
        choice = int(input("Please select one of the following: \n1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit\n What is your choice: "))
        if choice == 1:
            item_add = input("What is the item to add in the list: ")
            price_add = float(input("What is the price of the new item: "))
            # Store the price as a float, not a formatted string
            shopping_cart.append(item_add)
            price_list.append(price_add)
            print(f"{item_add} has been added to the cart")
        elif choice == 2:
            for i in range(len(shopping_cart)):
                # Format the price when displaying it, not when storing it
                formatted_price = "{:.2f}".format(price_list[i])
                print(f"{i}. {shopping_cart[i]} ${formatted_price}")
        elif choice == 3:
            # Implement the logic for removing an item
            item_to_remove = int(input("Enter the index of the item to remove: "))
            if 0 <= item_to_remove < len(shopping_cart):
                removed_item = shopping_cart.pop(item_to_remove)
                removed_price = price_list.pop(item_to_remove)
                print(f"{removed_item} has been removed from the cart")
            else:
                print("Invalid index")
        elif choice == 4:
            # Sum the list of float prices
            total = sum(price_list)
            formatted_total = "{:.2f}".format(total)
            print(f"Your total is ${formatted_total}")
        elif choice == 5:
            print("You have successfully opted out.")
            break
    except ValueError:
        print("Invalid input. Please enter a number corresponding to your choice.")

                               