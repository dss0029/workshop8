def calc(x, y, operation):
    valid_operations = ['+', '-', '*', '/']
    if not (isinstance(x, int) or isinstance(x, float)) or not (isinstance(y, int) or isinstance(y, float)):
        result = "ERROR: Input must follow format of (number, number, operation)"
        print(result)
        return result
    if operation not in valid_operations:
        result = "ERROR: Valid operations are +, -, *, and /"
        print(result)
        return result
    if operation == '+':
        result = addition(x, y)
    elif operation == '-':
        result = subtraction(x, y)
    elif operation == '*':
        result = multiplication(x, y)
    elif operation == '/':
        result = division(x, y)
    return result


def addition(x, y):
    result = x + y
    return result


def subtraction(x, y):
    result = x - y
    return result


def multiplication(x, y):
    result = x * y
    return result


def division(x, y):
    if y == 0:
        result = "ERROR: Cannot divide by 0"
        print(result)
        return result
    result = x / y
    return result


if __name__ == '__main__':
    calc(1, .5, '+')
