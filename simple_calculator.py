# This program implements a simple calculator that can perform basic arithmetic operations.
# Implementing basic operators, functions, user input.

def add(num1, num2):
    output = num1 + num2
    print(output)
    return output

def sub(num1, num2):
    output = num1 - num2
    print(output)
    return output

def mul(num1, num2):
    output = num1 * num2
    print(output)
    return output

def div(num1, num2):
    if num2 != 0:
        output = num1 / num2
    else:
        output = f"Second operand can not be zero."
    print(output)
    return output

def f_div(num1, num2):
    if num2 != 0:
        output = num1 // num2
    else:
        output = f"Second operand can not be zero."
    print(output)
    return output

def rem(num1, num2):
    if num2 != 0:
        output = num1 % num2
    else:
        output = f"Second operand can not be zero."
    print(output)
    return output

def exp(num1, num2):
    output = num1 ** num2
    print(output)
    return output

def operation_on_nums(operation, num1, num2):
    if operation == '+':
        add(num1, num2)
    elif operation == '-':
        sub(num1, num2)
    elif operation == '*':
        mul(num1, num2)
    elif operation == '/':
        div(num1, num2)
    elif operation == '//':
        print(f"First converting nums into integers.")
        f_div(int(num1), int(num2))
    elif operation == '%':
        print(f"First converting nums into integers.")
        rem(int(num1), int(num2))
    elif operation == '**':
        exp(num1, num2)
    else:
        print(f"Invalid operation....our program does not support {operation} operation yet.")


while True:
    operation = input("Enter operation (+, -, *, /, %, //, **): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    query_check = input(f"Do you want to perform {num1} {operation} {num2}? (yes/no): ")
    if query_check.lower() == 'yes':
        operation_on_nums(operation, num1, num2)
        another_query = input("Wanna do once more? (y/n) : ")
        if another_query.lower() == 'y':
            continue
        elif another_query.lower() == 'n':
            print("See you again!!🥺")
            break
        else:
            print("Invalid entry.")
    elif query_check.lower() == 'no':
        print("Hmm...let's take input again.")
    else:
        print("Invalid entry.")
