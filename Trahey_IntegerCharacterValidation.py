# PART 1
# Integer input

print(' ')
print("Data validation routines for integer and character")
print("--------------------------------------------------")
print(' ')

while True:
    userInput = input("Enter an integer >= 0: ")
    
    if userInput.isdigit():
        integerValue = int(userInput)
        if integerValue >= 0:
            print(f"You entered integer: {integerValue}")
            break
    else:
        print("Invalid Entry. Try again.")

# PART 2
# Character input

validchars = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'f', 'F']
while True:
    charinput = input("Enter a character a-f (excluding 'e'), upper or lower case: ")
    
    if len(charinput) == 1 and charinput in validchars:
        print(f"You entered character: {charinput.upper()}")
        break
    else:
        print("Invalid Entry. Try again.")