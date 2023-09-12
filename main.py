
choice = input("choose [*,+,-,/]: ")


if choice == '*':
    num1 = int(input("enter the first number :"))
    num2 = int(input("enter the second number :"))
    total = num1 * num2 
    print(f"{num1}*{num2}={total}")

elif choice  == '+':
    num1 = int(input("enter the first number :"))
    num2 = int(input("enter the second number :"))
    total= num1 + num2 
    print(f"{num1}+{num2}={total}")
elif choice == '-':
    num1 = int(input("enter the first number :"))
    num2 = int(input("enter the second number :"))
    total = num1 - num2 
    print(f"{num1}-{num2}={total}")
elif choice == '/':
    num1 = int(input("enter the first number :"))
    num2 = int(input("enter the second number :"))
    if num2 == 0:
        print('Zero not allowed , try again ')
    else:
        total = num1 / num2 
        print(f"{num1}/{num2}={total}")
else:
    print(" ERROR ERROR ERROR")




