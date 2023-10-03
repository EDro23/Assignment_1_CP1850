"""Tip Calculator program!
    Designed by Ethan Drover"""

print("Tip Calculator\n") # Header for the program
cost = float(input("Cost of meal: ")) # Input cost of meal from end user

print("\n15%")
print("Tip amount:\t  {:.2f}".format(cost * .15))           # Print statement for 15%
print("Total amount: {:.2f}".format(cost * .15 + cost))

"""Original cost X .15 gives you your tip amount for 15%
Original cost X .15 + original cost gives you your original cost plus the tip amount for 15%
Repeat for 20% and 25%"""

print("\n20%")
print("Tip amount:\t  {:.2f}".format(cost * .20))           # Print statement for 20 percent
print("Total amount: {:.2f}".format(cost * .20 + cost))

print("\n25%")
print("Tip amount:\t  {:.2f}".format(cost * .25))           # Print statement for 25 percent
print("Total amount: {:.2f}".format(cost * .25 + cost))

# End of program