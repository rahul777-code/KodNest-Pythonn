# accepts 2 user inputs from user and then accept operation (+,-,*,/) according to the operation provided execute the necessary operation
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation=='+':
    print(num1+num2)
elif operation=='-':
    print(num1-num2)
elif operation=='*':
    print(num1*num2)
elif operation=='/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error: Division by zero")
else:
        print("Invalid operation")
