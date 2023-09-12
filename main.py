while True:
    choice = input("Choose [*, +, -, /] (or type 'exit' to quit): ")

    if choice == 'exit':
        break

    if choice in ['*', '+', '-', '/']:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        if choice == '*':
            total = num1 * num2
            print(f"{num1}*{num2} = {total}")
        elif choice == '+':
            total = num1 + num2
            print(f"{num1}+{num2} = {total}")
        elif choice == '-':
            total = num1 - num2
            print(f"{num1}-{num2} = {total}")
        elif choice == '/':
            if num2 == 0:
                print('Zero not allowed, try again.')
            else:
                total = num1 / num2
                print(f"{num1}/{num2} = {total}")
    else:
        print("ERROR: Invalid choice. Please choose from [*, +, -, /] or type 'exit'.")





