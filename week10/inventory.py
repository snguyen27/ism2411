
#----------Self-Assessment-----------

#1. We have touched on the list topic for a little bit in the previous chapter, so there are not a lot of things that were new to me. However, I did not know that we could edit the list by using command such as remove or append.

#2. One real business situation could be tracking daily sales for a store. Instead of manually entering and calculating sales in Excel, I could use a Python list to store each day's sales, calculate the total and average.

#-----------Exercise 1--------------

# inventory = ["pen", "notebook", "stapler", "tape", "marker"]

# print(inventory)
# print(len(inventory))

#---------Exercise 2---------------

# inventory = ["pen", "notebook", "stapler", "tape", "marker"]

# print(inventory[0])
# print(inventory[-1])
# print(inventory[len(inventory) // 2])

#---------Exercise 3---------------

# inventory = ["pen", "notebook", "stapler", "tape", "marker"]

# print(inventory[:3])
# print(inventory[-2:])
# print(inventory[::2])

#---------Exercise 4------------

# inventory = ["pen", "notebook", "stapler", "tape", "marker"]

# inventory.append("envelop")
# print(inventory)

# inventory.remove("tape")
# print(inventory)

# inventory.sort()
# print(inventory)

#----------Exercise 5----------

# coords = (40.7128, -74.0060)

# try:
#     coords[0] = 99
# except TypeError:
#     print("Tuples are useful for coordinates because they cannot be changed accidentally.")

# print(coords)

#-----------Exercise 6------------

# sales = [100, 250, 75, 480, 200]

# #Calculate total, count, and average
# total = sum(sales)
# count = len(sales)
# average = total / count

# # Find best and worst sales days
# best = max(sales)
# worst = min(sales)

# print(f"Total: {total}")
# print(f"Count: {count}")
# print(f"Average: {average}")
# print(f"Best: {best}")
# print(f"Worst: {worst}")

#------------Exercise 7--------------

# prices = [9.99, 14.99, 4.99, 24.99, 1.99]

# discounted = []

# for price in prices:
#     new_price = round(price * 0.90, 2)
#     discounted.append(new_price)

# print(f"Original: {prices}")
# print(f"Discounted: {discounted}" )

#----------Exercise 8---------------

# sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

# high_sales = []

# for sale in sales:
#     if sale > 300:
#         high_sales.append(sale)

# count = len(high_sales)
# average = sum(high_sales) / count

# print(high_sales)
# print(f"Count: {count}")
# print(f"Avg: ~{average:.2f}")