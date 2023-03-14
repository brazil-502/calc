# calc
# developed by: brazil
# author url: no money to purchase a domain :sad:
# version: 1.0

print("Select an operation to perform: ")
print("+ = ADD")
print("- = SUBTRACT")
print("* = MULTIPLY")
print("/ = DIVIDE")

operation = input("enter a operation:- ")

if operation == "+":
    # code for add
    num1 = int(input("enter ur value: "))
    num2 = int(input("enter ur value: "))
    num3 = num1+num2
    print(num3)
elif operation == "-":
    # code for sub
    num1 = int(input("enter ur value: "))
    num2 = int(input("enter ur value: "))
    num3 = num1 - num2
    print(num3)
elif operation == "*":
    # code for multi
    num1 = int(input("enter ur value: "))
    num2 = int(input("enter ur value: "))
    num3 = num1 * num2
    print(num3)
elif operation == "/":
    # code for div
    num1 = int(input("enter ur value: "))
    num2 = int(input("enter ur value: "))
    num3 = num1 / num2
    print(num3)
else:
    print("invalid syntax, try again")
    #dum dum helping