import random
namestring=input("enter the name of cardholder ")
name=namestring.split(",")
print(name)
choice=len(name)
print(choice)
billpayment=random.randint(0,choice-1)
print(billpayment)

