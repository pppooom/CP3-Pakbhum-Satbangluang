menuList = []

def showBill():
    print("-----Hello myShop-----")
    print("----สรุปรายการอาหารที่สั่ง----")
    for i in range(len(menuList)):
        print(menuList[i]," THB")
    sum = 0
    for j in range(len(menuList)):
        sum += menuList[j][1]
    print("Total sum :", sum, "THB")
''' 
def sumPrice():
    sum = 0
    for i in range(len(menuList)):
        sum += menuList[i][1]
    print("Total sum :",sum,"THB")

'''

while True:
    menuName = input("Please enter menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append([menuName,int(menuPrice)])

print(str(menuList))
showBill()
#sumPrice()

