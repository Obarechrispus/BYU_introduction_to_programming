"""
Author: Chrispas Obare Moraa
A simple shopping cart program for a shopping list
"""
replace = ''
items = ""
item_list = ["kj", "gfd", "gfhgh", "hgj", "gfhg"]

while True:
    replace = input("Which item would you like to change? Choose a number from 0 to {} or type 'none' if you are good with what you chose: ".format(len(item_list) - 1)).lower()
    
    if replace == "none":
        print("No changes made.")
        break

    
    replace = int(replace)
    #except ValueError:
        #print("Invalid input. Please enter a valid number or 'none'.")
       # continue

    if 0 <= replace < len(item_list):
        item_list.pop(replace)
        new = input("Do you wish to exchange it with another item? (yes or no): ").lower()
        if new == 'yes':
            new_item = input("What is the new item: ")
            item_list.insert(replace, new_item)
            print("Updated list:", item_list)
        elif new == 'no':
            print("Item removed. Updated list:", item_list)
        else:
            print("Invalid response. No changes made.")
    else:
        print("Invalid index. Please choose a number between 0 and {}.".format(len(item_list) - 1))
