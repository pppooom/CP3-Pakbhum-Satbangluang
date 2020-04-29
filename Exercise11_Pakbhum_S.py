inputNumber = int(input())
for x in range(inputNumber):
    text = ""
    for y in range(((x+1)*2)-1):
        text = text+"*"
        z = " "
        z = ((inputNumber-1)-x) * " "
    print(z+text)