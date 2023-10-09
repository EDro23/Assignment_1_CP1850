""" Table of powers program!
    Designed by Ethan Drover."""

calc = True
while calc:
    print("Table of Powers\n") # Header
    start = int(input("Start number: "))
    stop = int(input("Stop number:  "))
    line = "="
    
    if start > stop:        # If user enters invalid data it prints this message
        print("Start number must be less than stop number\nPlease try again.")
        calc = False
        
    else:               # Format for when user enters valid data
        print("\nNumber\t\tSquared\t\tCubed")
        print("{}\t\t{}\t\t{}".format(line*6,line*7,line*5))
        
        for number in range(start,stop + 1):
            squared = number ** 2
            cubed = number ** 3
   
            print("{}\t\t\t{}\t\t{}".format(number,squared,cubed)) # Print statement

            calc = False # End of program