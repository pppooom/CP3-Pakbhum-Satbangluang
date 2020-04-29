def login():
    username = input("Username : ")
    password = input("Password : ")
    if (username == "pakbhum" and password == "12345"):
        return True
    else:
        return False
def showMenu():
    print("----Pakbhum Shop----")
    print("1.Vat Calculator")
    print("2.Price Calculator")
def menuSelect():
    userSelected = int(input(">>" ))
    if (userSelected==1 ):
        totalPrice = int(input("Total price :"))
        vatCalculate(totalPrice)
    elif(userSelected==2):
        priceCalculate()
    else:
        print("Please select only the given number")

def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return print("The result is :",result)
def priceCalculate():
    price1 = int(input("first Product price: "))
    price2 = int(input("Second product prrice: "))
    return "The result is: ",vatCalculate(price1 + price2)

'''

คำสั่งการหลักเริ่มจากตรงนี้เป็นต้นไป

'''

if (login()):
    print("Welcome!")
    showMenu()
    menuSelect()

else :
    print("Please Check user and Password")



