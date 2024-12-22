nput("Enter the first number: ")
num2 = input("Enter the second number: ")
operation1 = input("Choose the operation (+, -, *, /): ")

try:
    num1 = float(num1)
    num2 = float(num2)

    match operation1:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            if num2 != 0:
                result = num1 / num2
            else:
                raise ZeroDivisionError("Division by zero")
        case _:
            raise ValueError("Invalid operation")

    print(f"The result is: {result}")

except ValueError as e:
    print(f"Error: {e}")
except ZeroDivisionError as e:
    print(f"Error: {e}")num2 = input("Enter the second number: ")
