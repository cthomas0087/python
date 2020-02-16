##make a calculator using IF statements and user input


num1=int (input("enter a  number: "))
cmd= input('enter a math function (+, -, *, /) : ')
num2=int (input("enter a second number: "))

if cmd == '+':
    print(num1 + num2)

elif cmd == '-':
    print(num1 - num2)

elif cmd == '*':
    print(num1 * num2)

elif cmd == '/':
    print(num1 / num2)

else:
    print("error, your input is invalid, try again.")



    
