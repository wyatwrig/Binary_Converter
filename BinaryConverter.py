import math

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

def getNumber():
    return int(input("Enter a number: "))

def binaryToDecimal():
    number = getNumber()
    binary = 0
    totalDigits = int(math.log10(number)) + 1
    digitsArray = [int(i) for i in str(number)]

    for digit in digitsArray:
        if (digit == 1):
            binary += (pow(2, totalDigits) - 1)
        totalDigits -= 1

    print(str(number) + " is " + str(binary) + " in decimal.")


def decimalToBinary():
    number = getNumber()

conversionType()