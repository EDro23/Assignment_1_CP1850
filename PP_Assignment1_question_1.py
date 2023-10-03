""" Letter grade converter program!
    By Ethan Drover."""

print("Letter Grade Converter") #Header for program

program = True
while program:
    grade_int = int(input("\nEnter numerical grade:  ")) #User input entered by user
    
    if grade_int >= 88 and grade_int <= 100:
        grade_int = "A"
    elif grade_int >= 80 and grade_int <= 87:               # "If" and "Elif" statements created to turn integers into numbers.
        grade_int = "B"
    elif grade_int >= 67 and grade_int <= 79:   
        grade_int = "C"
    elif grade_int >= 60 and grade_int <= 66:
        grade_int = "D"
    else:
        grade_int = "F"
    print("Letter Grade: {}".format((grade_int))) # Output to console displaying the user thier grade as a letter.
    
    if input("\nContinue? (y/n): ") != 'y' and 'Y':
        break

print("\nBye!") # End of program statement.