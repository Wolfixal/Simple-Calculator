inputNo = int(input("How many values would you like to input? (value has to be 2 or above): "))

if inputNo < 2:
    print("insufficient values")
    quit()

if inputNo >= 2:
    x = float(input("Input a value: "))
    operator = input("Input an operator (*,/,+,-): ")
    y = float(input("Input a second value: "))

    if operator == "*":
        product = x*y
        inputNo = inputNo - 2

    if operator == "/":
        product = x/y
        inputNo = inputNo - 2


    if operator == "-":
        product = x-y
        inputNo = inputNo - 2
        


    if operator == "+":
        product = x+y
        inputNo = inputNo - 2

while inputNo >= 1:
    operator = input("Input an operator (*,/,+,-): ")
    x = float(input("Input another value: "))

    if operator == "*":
        product = product*x
        inputNo = inputNo - 1
        continue

    if operator == "/":
        product = product/x
        inputNo = inputNo - 1
        continue

    if operator == "-":
        product = product-x
        inputNo = inputNo - 1
        continue


    if operator == "+":
        product = product+x
        inputNo = inputNo - 1
        continue



if inputNo == 0:
    print("The answer is:",product)