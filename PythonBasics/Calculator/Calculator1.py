from art import logo

def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def devide(n1,n2):
    return n1/n2

operators = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": devide
}
def calculator():
    print(logo)
    number1 = float(input("what is the first number: "))
    continue_with_result = "y"
    while continue_with_result == 'y':
        for symbol in operators:
            print(symbol)

        selected_operation = input("pick any selected_operation input from above option: ")
        number2 = float(input("what's next number: "))
        result = operators[selected_operation](number1,number2)
        print(f"{number1} {selected_operation} {number2} = {result}")
        continue_with_result = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation ").lower()

        if continue_with_result == 'y':
            number1 = result
        elif continue_with_result == 'n':
            print("\n"* 20)
            calculator()

calculator()