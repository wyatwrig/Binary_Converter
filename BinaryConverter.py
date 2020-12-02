import math
## This is a simple program to convert between decimal and binary numbers.

# conversionType is a repl that determines which way the user wants to translate.
def conversionType():
    choice = '0'
    while (choice != '3'):
        print("Choose an option:")
        print("1. Binary to Decimal")
        print("2. Decimal to Binary")
        print("3. Quit")
        choice = input(">>")
        if (choice == '1'):
            binaryToDecimal()
        elif (choice == '2'):
            decimalToBinary()
        elif (choice == '3'):
            print("Exiting...")
            return
        else:
            print("Not a Valid Choice")

# Helper function to get a numerical input from the user
def getNumber():
    return int(input("Enter a number: "))

#Converts a binary number to decimal and prints result.
def binaryToDecimal():
    number = getNumber()
    decimal = 0
    totalDigits = int(math.log10(number)) + 1 #Find number of digits
    digitsArray = [int(i) for i in str(number)] #Add each digit (1 or 0) to an array

    for digit in digitsArray:
        if (digit == 1):
            decimal += (pow(2, totalDigits-1)) #If there is a one in the digits array, add 2^(digit's place) to binary.
        totalDigits -= 1

    print(str(number) + " is " + str(decimal) + " in decimal.")

#converts a decimal number to binary and prints result.
def decimalToBinary():
    number = getNumber()
    holdingNumber = number
    bits = []
    while (holdingNumber/2 != 0): #divide by two until zero to evaluate each digit.
        bits.append(int(holdingNumber % 2)) #The remainder signifies if a bit is flipped.
        holdingNumber = int(holdingNumber/2)

    bits.reverse() #digits come out backwards, need to be flipped.

    binary = ""
    for bit in bits:
        binary += str(bit) #pull digits out of array

    print(str(number) + " is " + binary + " in binary.")

conversionType()