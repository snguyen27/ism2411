#------------Self-Assessment--------------

#1. I only found out the bug after asking AI. For the 2nd bug, it tells me that I need to pay attention to details, and that VS code litterally underline that part, but I didn't pay attention to that part. For the 1st and 3rd bug, 
#it tells me that my knowledge about this specific topic is not enough for me to be able to spot out what's wrong with it. 

#2. apply_discount(price, tier) means that it is the name of the function. Price and tier are parameters, which means that price and tier are in the equation. 
# It would return the price of a product after getting discount. I don't think a colleague could use it without reading the body because there is no equation for it.

#3. AI used on question 3 and 5. AI did deepen my understanding, but I need to do some more practice and ask it some more questions to actually understand what it was saying.

#----------Exercise 1--------------

# Defining a function
def calculate_tax(price, rate):
    return price * rate

#Calling the function
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")


#-----------Exercise 2------------

#Defining a function with different parameters
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

#calling the function with different tiers
original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

#-------------Exercise 3------------------
def calculate_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    return price

def calculate_tax(price, rate):
    return price * rate

def final_price(price, tier, tax_rate):
    discounted_price = calculate_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

#Callinv the final_price function
after_discount = calculate_discount(200, "gold")
print(f"After gold discount: ${after_discount:.2f}")

tax = calculate_tax(after_discount, 0.07)
print(f"After tax: ${after_discount + tax:.2f}")

print(f"final_price(200, 'gold', 0.07) = ${final_price(200, 'gold', 0.07):.2f}")

#-----------Exercise 4--------------------

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")



#-----------Exercise 5---------

# broken_sales.py - trace and diagnose before fixing anything.
# sales = [120, 80, 250, 175, 90]

# total = 0
# for sale in sales:
#     total = sale
# print(f"Total: ${total}")

# count = 0
# for sale in sales
#     count += 1
# print(f"Count: {count}")

# i = 0
# while i <= len(sales):
#     print(sales[i])
#     i += 1

# Bug #1, the goal of the 1st part is to find the sum, which is 120+80+250+175+90, but because we use 
# total = sale, the result is 90 instead. 
# "+=" means "add to the existing value"

#The second bug is that it is missing a colon

#The 3rd bug is there are only 4 index in the racket, but "<=" is asking for the 5th one which doesnt exist. 
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1

#----------Exercie 6------------

x= 100    # global x

def double_it():
    x = 999     # local x
    return x * 2

print(x)
print(double_it())
print(x)

# print(x) would give 100
# print(double_it()) would give 1998
# # print(x) would give 100



















