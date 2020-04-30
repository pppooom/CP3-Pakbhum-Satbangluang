'''ไม่รู้ว่าผู้ใช้งานจะกรอกกี่รอบจนกว่าจะ exit'''
'''  .lower() ข้อมูลเป็นตัวเล็กทั้งหมด'''
'''สร้าง List เปล่าๆ มาเพื่อเก้บข้อมูล'''
''' ข้อมูลตัวเลขควรแบ่งแยกกับข้อมูลชื่อ ซึ่งควรตั้ง list ม่ใหม่เป็น priceList'''
'''การเปลี่ยนข้อมูลใน list ที่เป็น stringเป็น int ทำได้โดย priceList[i] = int(priceList[i])'''
menuList = []
priceList = []
def showBill():
    print("-----Hello myShop-----")
    print("----สรุปรายการอาหารที่สั่ง----")
    sum = 0
    for i in range(len(menuList)):
        print(menuList[i],priceList[i]," THB")
        priceList[i] = int(priceList[i])
        sum = sum + priceList[i]
    print("Total sum :",sum,"THB")

while True:
    menuName = input("Please enter menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)

print(str(priceList))
showBill()






