def calculator(a, b, operator):


    try:
        if operator == '+':
            return a+b
        elif operator == '-':
            return a-b
        elif operator == '/':
            if b == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return a / b
        elif operator == '*':
            return a * b
        elif operator == "%":
            if b == 0:
                raise ZeroDivisionError("Modulo by zero is not allowed.")
            return a % b
        elif operator == "**":
            return a ** b
        else:
            raise ValueError("Unsupported operator.")


    except ZeroDivisionError as zde:
        return f"Error: {zde}"

    except ValueError as ve:
        return f"Error: {ve}"

    except TypeError:
        return "Error: Invalid input type. Please provide numeric values."

    except Exception as e:
        return f"Error: Unexpected error occurred - {e}"


print(calculator(10, 0, "/"))
print(calculator(10, "five", "+"))
print(calculator(10, 5, "$"))