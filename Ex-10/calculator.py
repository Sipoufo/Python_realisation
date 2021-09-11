from art import logo

# Addition
def addition(n1, n2):
    return n1 + n2

# Subtraction
def soustraction(n1, n2):
    return n1 - n2

# Multiplication    
def multiplication(n1, n2):
    return n1 * n2

# Division
def division(n1, n2):
    return n1 / n2

operations = {
    "+" : addition,
    "-" : soustraction,
    "*" : multiplication,
    "/" : division
}



print(logo)
continues = True
continues_cal = "n"
while continues:
    
    if continues_cal == "n":
        num1 = float(input("What's your first number?: "))

        for operation in operations:
            print(operation)
        
        operation_symbol = input("Pick an operation from the list above: ")
        num2 = float(input("What's your second number?: "))
        operation_function = operations[operation_symbol]
        result = operation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        continues_cal = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    else:
        for operation in operations:
            print(operation)
        operation_symbol = input("Pick an another operation : ")
        num3 = float(input("What's the next number?: "))
        operation_function = operations[operation_symbol]
        result2 = operation_function(result, num3)
        print(f"{result} {operation_symbol} {num3} = {result2}")

        continues_cal = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if continues_cal == "y":
            result = result2
            