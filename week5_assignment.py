"""
Author: Chrispas Obare Moraa
A simple shopping cart program for a shopping list
"""
price_list = []
shoping_cart = []
number = 1

while True:
    try:
        choice = int(input("Please select one of the following: \n1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit\n What is your choice: "))
        if choice == 1:
            item_add = input("what is the item to add in the list: ")
            price_add = float(input("what is the price of the new: "))
            #formated_price = "{:.2f}".format(price_add)
            shoping_cart.append(item_add)
            price_list.append(price_add)
            print(f"{item_add} has been added to cart")
        elif choice == 2:
            for i in range(len(shoping_cart)):
                print(f"{i + number}. {shoping_cart[i]} ${price_list[i]}")
        elif choice == 3:
            item_to_remove = int(input("Enter the index of the item to remove: "))
            if 0 < item_to_remove < len(shoping_cart):
                removed_item = shoping_cart.pop(item_to_remove - 1)
                removed_price = price_list.pop(item_to_remove - 1)
                print(f"{removed_item} has been removed from the cart")
            else:
                print("Invalid index")
        elif choice == 4:
            sum_shopping = sum(price_list)
            convert_sum = "{:.2f}".format(sum_shopping)
            print(f"Your totals are ${convert_sum} ")
        elif choice == 5:
            print("You have succefully opted out, ")
            break
    except ValueError:
        print("Wrong choice")