from tkinter import *
import math

def leftClickButton(event):
    result = int(textBoxWeight.get())/math.pow(int(textBoxHeigth.get())/100,2)
    print(int(result))
    if result > 30:
        labelResult.configure(text="อ้วนมาก")
    elif result >= 25.0 and result <= 29.9:
        labelResult.configure(text="อ้วน")
    elif result >= 23.0 and result <= 24.9:
        labelResult.configure(text="น้ำหนักเกิน")
    elif result >= 18.6 and result <= 22.9:
        labelResult.configure(text="น้ำหนักปกติ เหมาะสม")
    else :
        labelResult.configure(text="ผอมเกินไป")

MainWindow = Tk()
labelHeigth =  Label(MainWindow,text = "ส่วนสูง (cm.)")
labelHeigth.grid(row =0, column = 0)
textBoxHeigth =Entry(MainWindow)
textBoxHeigth.grid(row =0, column =1)
labelWeight = Label(MainWindow,text = "น้ำหนัก (kg.)")
labelWeight.grid(row =1 , column =0)
''' ถ้าใช้ grid ในคำสั่งเลยจะไม่สามารถใช้ get ได้ เพราะ type ไม่ใช่แบบ entry ต้องสั่งแยก'''
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)

calculateButton = Button(MainWindow,text= "คำนวน")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row =2 , column =0)
labelResult = Label(MainWindow,text = "ผลลัพธ์")
labelResult.grid(row=2,column =1)

MainWindow.mainloop()


