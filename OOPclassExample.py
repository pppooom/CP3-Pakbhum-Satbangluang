'''
customerName = ""
customerLastName = ""
ถ้าทำแบบนี้จะสร้างเก็บ ชื่อ-นามสกุลของ customer ได้ไม่ดีพอ
*ลองใช้การเขียนเชิงวัตถุ โดยการสร้างแบบ class = แบบแปลนหรือรูปแบบให้กับฟังก์ชันของเรา
'''

class Customer:
    '''name หรืออื่นๆคือ attribute'''
    name = ""
    lastName = ""
    age = 0

    '''สร้างฟังก์ชันขึ้นมาโง่ๆอันหนึ่ง โดจจะมี parameter "self" มาให้อัตโนมัติทันทีเลย'''
    def addCart(self):
        print("Add to Cart",self.name,self.lastName+"'s cart")

customer1 = Customer()
'''ไลน์ด้านบนคือการเอาแปลนมาสร้าง Object ขึ้นมาใช้งานได้จริงๆ แล้วแต่ว่าจะเอาไปใช้ทำอะไร'''
customer1.name = "Pakbhum"
customer1.lastName = "Satbangluang"
'''customer1 หมายถึงลูกค้าคนที่ 1 เป็นคนเดียวเท่านั้น ถ้าเราจะเข้าไปยุ่งเกี่ยวหรือจัดการอะไรก็ตามเกี่ยวกับลูกค้าคนนี้จะต้องใช้ customer1'''
customer1.addCart()

customer2 = Customer()
customer2.name = "Kanisorn"
customer2.lastName = "Jaruchapong"
customer2.addCart()

customer3 = Customer()
customer3.name = "Jakra"
customer3.lastName = "Wongsupprasert"
customer3.addCart()

customer4 = Customer()
customer4.name = "Surathee"
customer4.lastName = "Sitthi"
customer4.addCart()