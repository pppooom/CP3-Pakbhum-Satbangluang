inputNumber = int(input("Enter the number : "))

def vatCalculate(intputNumber):
    result = intputNumber+(intputNumber*(7/100))
    return result

print("Total price :",vatCalculate(inputNumber))