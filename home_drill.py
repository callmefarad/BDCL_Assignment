# A man went to a super market with an unknown amount of money, he bought three
# items(soap, milk and juice) and came back with a balance.
# Write a dynamic program that interprets the whole process
# displaying the balance he came back with.

# Enter your solution here:
# enter the capital
capital = float(input("Enter the amount taken to the super market: "))

# enter the amount of the different product
soap = float(input("Enter the amount of soap bought: "))
milk = float(input("Enter the amount of milk bought: "))
juice = float(input("Enter the amount of juice bought: "))

# sum the product bought
total_ammount_product = soap + milk + juice

# display the balance
balance = capital - total_ammount_product

print(balance)


