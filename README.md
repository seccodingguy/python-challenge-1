# Module 2 Assignment

# By: Mark Wireman

The assignment is a terminal based ordering system. The ordering system is a menu of food items to purchase from the local diner.

There is no limit to the number of menu items and quantity to purchase.

To use, run the following command from the main folder:

python menu.py

You'll be prompted for the menu item to purchase from:

From which menu would you like to order? 
1: Snacks
2: Meals
3: Drinks
4: Dessert

After selecting the item number, a list of food options is displayed (in this example Dessert was selected):

You selected Dessert
What Dessert item would you like to order?
Item # | Item name                | Price
-------|--------------------------|-------
1      | Chocolate lava cake      | $10.99
2      | Cheesecake - New York    | $4.99
3      | Cheesecake - Strawberry  | $6.49
4      | Australian Pavlova       | $9.99
5      | Rice pudding             | $4.99
6      | Fried banana             | $4.49

You will then select the quantity to purchase and asked if you would like to add more items (in this example Rice Pudding was selected with a quantity of 6).

Type menu Item # to order or q to quit: 5
Please enter the number of items to purchase: 6
Rice pudding
Would you like to keep ordering? (Y)es or (N)o n
Thank you for your order.
This is what we are preparing for you.

When the ordering is complete, a detailed list of the items ordered, subtotal, and final totals are displayed:

Item name                 | Price  | Quantity | Subtotal
--------------------------|--------|----------|-----------
Banana                     $0.69     3          $2.07
Burger - Beef              $8.49     5          $42.45
Rice pudding               $4.99     6          $29.94
 
                                   | Total Quantity | Order Total
                                     14                $74.46