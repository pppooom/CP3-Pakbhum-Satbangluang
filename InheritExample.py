class Vehicle:
    licneseNumber = ""
    serialCode = ""

    def turnOnAirConditioner(self):
        print("turn on Air")

class Car(Vehicle):
    pass

class PickUp(Vehicle):
    def sayWow(self):
        print("Wow Amazing")

class Van:
    '''เพราะมันเหมือนกันกับรถทั่วไป (Car) เลยก็อบมาได้เลย'''
    licneseNumber = ""
    serialCode = ""
    '''เพราะการเปิดแอร์เป็นฟังก์ชัน'''
    def turnOnAirConditioner(self):
        print("turn on Air")

class EstateCar:
    '''เพราะมันเหมือนกันกับรถทั่วไป (Car) เลยก็อบมาได้เลย'''
    licneseNumber = ""
    serialCode = ""
    '''เพราะการเปิดแอร์เป็นฟังก์ชัน'''
    def turnOnAirConditioner(self):
        print("turn on Air")

'''รวมความเป้นยานพหะนะที่เหมือนกันไว้ในน class นี้ class เดียว'''
''' 
ถ้าเอาไว้ข้างล่างจะ error ต้องทำงานจากบนสุด
class Vehicle:
    licneseNumber = ""
    serialCode = ""

    def turnOnAirConditioner(self):
        print("turn on Air")
'''

car1 = Car()
car1.turnOnAirConditioner()


car2 = PickUp()
car2.turnOnAirConditioner()
car2.sayWow()

car3 = Van()
car3.turnOnAirConditioner()

car4 = EstateCar()
car4.turnOnAirConditioner()
