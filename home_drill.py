# A man went to a super market with an unknown amount of money, he bought three
# items(soap, milk and juice) and came back with a balance.
# Write a dynamic program that interprets the whole process
# displaying the balance he came back with.

# Enter your solution here:





# let the unknown amount be #2000
# contributed  by gideon, joshua, yusuf

x = 2000
items = ['soap', 'milk', 'juice']
price_soap = 200
price_milk = 500
price_juice = 300
total = price_soap + price_milk + price_juice
balance = x - total
print("this is the balance",balance)
