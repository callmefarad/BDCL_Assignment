""" A man went to a super market with an unknown amount of money, he bought three
 items(soap, milk and juice) and came back with a balance.
 Write a dynamic program that interprets the whole process
 displaying the balance he came back with.
"""
# Enter your solution here:
totalAmount = float(input("Enter the amount of money: "))
soap = float(input("Enter the price of soap: "))
juice = float(input("Enter the price of juice: "))
milk = float(input("Enter the price of milk: "))

items = soap + juice + milk

Balance = totalAmount - items

print("The  balance is: ", Balance)

print("COPYRIGHT: Emma, Lekan Ola")