print("Hello Welcome!")
print("Please Login")
username = input("Username : ")
password = input("Password : ")
if(username == "pakbhum" and password == "12345"):
    print("Good morning",username)
    print("-------Pakbhum Store-------")
    print("1.Orange     30$ ")
    print("2.Mango      40$ ")
    print("3.Apple      50$ ")
    fruitSelected = (input("Number : "))
    if(fruitSelected == "1"):
        fruitAmount = int(input("Enter the amount : "))
        total = 30 * fruitAmount
        print("Total price for Orange :",total)
    elif(fruitSelected == "2"):
        fruitAmount = int(input("Enter the amount : "))
        total = 40 * fruitAmount
        print("Total price for Mango  :",total)
    elif (fruitSelected == "3"):
        fruitAmount = int(input("Enter the amount : "))
        total = 50 * fruitAmount
        print("Total price for Apple :",total)
    else:
        print("Please select in given number")
else:
    print("Invalid Username or Password")



