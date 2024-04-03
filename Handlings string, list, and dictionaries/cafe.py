# List of cafe items
menu = ["latte", "earl grey", "croissant", "pastel de nata", "matcha latte", "pain au chocolat", "mousse au chocolat"]

# Dictionary showing the amount of stocks of each item
stock = {"latte": 78,
         "earl grey": 100,
         "croissant": 32,
         "pastel de nata": 16,
         "matcha latte": 47,
         "pain au chocolat": 20,
         "mousse au chocolat": 14}

# Dictionary showing the prices of each item
price = {"latte": 3.50,
         "earl grey": 2.50,
         "croissant": 1.50,
         "pastel de nata": 2.00,
         "matcha latte": 4.50,
         "pain au chocolat": 2.00,
         "mousse au chocolat": 2.50}

# Setting total stock to 0 for the loop
total_stock = 0

# Going through each item in the menu list and using the item as a key for the stock and price dictionary
for item in menu:
    item_value = (price[item] * stock[item]) # calculating the total cost of each item 
    print(f'{item.capitalize()} = £{str(item_value)}') # outputting the items and their total cost
    total_stock += item_value # adding the total cost of items together

# Outputting the overall cost of the stock
print(f'Total = £{str(total_stock)}')
