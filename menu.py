'''
Assignment: Module 2
Author: Mark Wireman
Class Number: AI-PT-EAST-OCTOBER-100724
'''

# Menu dictionary


menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

def print_menu_categories():
    categoryId = 1
    menu_items = {}
    
    for key in menu.keys():
        print(f"{categoryId}: {key}")
        # Store the film title associated with its menu item number
        menu_items[categoryId]=key
        # Add 1 to the menu item number
        categoryId += 1

    return menu_items


# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
customer_order = []
order_total = 0
quantity_total = 0

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    
    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = print_menu_categories()

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    
    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            
            # 2. Ask customer to input menu item number
            food_selection = input("Type menu Item # to order or q to quit: ")

            # Exit the loop if user typed 'q'
            if food_selection == 'q':
                exit()
            
            # 3. Check if the customer typed a number
            if food_selection.isdigit():

                # Convert the menu selection to an integer
                menu_selection = int(food_selection)

                 # 4. Check if the menu selection is in the menu items
                if menu_selection in menu_items:
                    
                    # Store the item name as a variable

                    # Already saved as the menu_selection from above

                    # Ask the customer for the quantity of the menu item

                    quantity = input("Please enter the number of items to purchase: ")


                    # Check if the quantity is a number, default to 1 if not
                    if quantity.isdigit():
                        quantity_selection = int(quantity)

                        if(quantity_selection < 1):
                            quantity_selection = 1

                    # Add the item name, price, and quantity to the order list

                    '''
                        {
                            "Item name": "string",
                            "Price": float,
                            "Quantity": int
                        },
                    '''
                    print(menu_items[menu_selection]["Item name"])
                    customer_order.append({"Item Name":menu_items[menu_selection]["Item name"],"Price":menu_items[menu_selection]["Price"],"Quantity":quantity_selection})
                    
                    # Tell the customer that their input isn't valid
                else:
                    print(f"{food_selection} was not a food option.")



            else:
                # Tell the customer they didn't select a menu option
                print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number. Try again.")
        exit()

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

       
        # 5. Check the customer's input

                # Keep ordering

                # Exit the keep ordering question loop

                # Complete the order

                # Since the customer decided to stop ordering, thank them for
                # their order

                # Exit the keep ordering question loop


                # Tell the customer to try again

        keep_ordering_choices = {"Y","N"}

        if keep_ordering.upper() in keep_ordering_choices:
            if keep_ordering.upper() == "N":
                place_order = False
                print("Thank you for your order.")
            else:
                place_order = True
            break
        else:
            print("Invalid input. Please try again (Ctrl-C to stop).")


# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
print(f'Check Structure: {customer_order}')
print(' ')
print(' ')

print("Item name                 | Price  | Quantity | Subtotal")
print_line = "--------------------------|--------|----------|-----------"
#print("--------------------------|--------|----------")
print(print_line)
# 6. Loop through the items in the customer's order
i = 0
for item_key, price_key, quantity_key in customer_order:

    # 7. Store the dictionary items as variables
    item_name = customer_order[i][item_key]
    item_quantity = customer_order[i][quantity_key]
    item_price = customer_order[i][price_key]
    item_total = item_quantity * item_price
    
    # 8. Calculate the number of spaces for formatted printing
    print_line_split = print_line.split('|')

    num_item_spaces = len(print_line_split[0]) - len(item_name)
    item_spaces = " " * num_item_spaces

    num_item_price_spaces = len(print_line_split[1])-len(str(item_price))
    item_price_spaces = " " * num_item_price_spaces

    num_item_quantity_spaces = len(print_line_split[2])-len(str(item_quantity))
    item_quantity_spaces = " " * num_item_quantity_spaces

    # 9. Create space strings
    item_name_with_spaces = item_name + item_spaces
    item_price_with_spaces = str(item_price) + item_price_spaces
    item_quantity_with_spaces = str(item_quantity) + item_quantity_spaces

    # 10. Print the item name, price, and quantity
    print(f'{item_name_with_spaces} ${item_price_with_spaces} {item_quantity_with_spaces} ${item_price*item_quantity}')
    
    i+=1


# 11. Calculate the cost of the order using list comprehension
total_order = sum([custorder["Quantity"] * custorder["Price"] for custorder in customer_order])
total_quantity = sum([custorder["Quantity"] for custorder in customer_order])

order_total_output = "                                   | Total Quantity | Order Total"
order_total_output_split = order_total_output.split('|')
print(' ')
total_item_spaces = (len(order_total_output_split[0]) + len(order_total_output_split[1])) - len(str(total_quantity))
total_item_quantity_spaces = " " * total_item_spaces
total_cost_spaces = " " * (len(order_total_output_split[1])-1)

# Multiply the price by quantity for each item in the order list, then sum()
print(order_total_output)
total_order_formatted = "{:.2f}".format(total_order)
# and print the prices.
print(f'{order_total_output_split[0]}  {total_quantity} {total_cost_spaces}${total_order_formatted}')