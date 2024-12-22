num1 = input("Enter the first number:")
num2 = input("Enter the second number:")
operation1 = input("choose the operation (+, -, *, /)")
match operation1:
    case '+':
        print(f"the result is: {num1 + num2}")
        
    case '-':
        print(f"the result is: {num1 - num2}")

    case '*':
        print(f"the result is: {num1 * num2}")

    case '/':
        if num2 != 0:
            print(f"the result is: {num1 / num2}")
        else:
            print("invalid division")
