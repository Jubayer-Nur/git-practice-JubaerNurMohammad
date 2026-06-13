def add(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Please provide numbers"

def subtract(a, b):
    try:
        return a - b
    except TypeError:
        return "Error: Please provide numbers"

def multiply(a, b):
    try:
        return a * b
    except TypeError:
        return "Error: Please provide numbers"

def divide(a, b):
    try:
        if b == 0:
            return "Error: Division by zero"
        return a / b
    except TypeError:
        return "Error: Please provide numbers"