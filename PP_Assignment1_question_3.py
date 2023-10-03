""" Change calculator program!
    designed by Ethan Drover"""

print("Change Calculator") # Header
program_run = True
c = 0 # Initial starting change set to 0

while program_run:
    c = int(input("\nEnter number of cents (0-99): ")) # input for the user, integer must be between 0-99
    print("\nQuarter(s): {}".format(c // 25))
    c = c % 25
    print("Dime(s):\t{}".format(c // 10))
    c = c % 10                                  # Calculations for converting the change.
    print("Nickle(s):  {}".format(c // 5))
    c = c % 5
    print("Pennie(s):  {}".format(c // 1))
    
    if input("\nContinue? (y/n):  ") != 'y' and 'Y':
        
        print("\nBye!")         # End of program statement.
        break