def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def devide(n1,n2):
    return n1/n2

continue_with_result = 'y'
number1 = int(input("what is the first number: "))
while continue_with_result == 'y':
    print("+ \n- \n* \n/")
    operation = input("pick any operation input from above option: ")
    number2 = int(input("what's next number: "))

    if(operation == '+'):
        result = add(number1, number2)
        print(f"{number1} + {number2} = {result}")
    elif(operation == '-'):
        result = sub(number1, number2)
        print(f"{number1} - {number2} = {result}")
    elif(operation == '*'):
        result = multiply(number1, number2)
        print(f"{number1} * {number2} = {result}")
    elif(operation == '/'):
        result = devide(number1, number2)
        print(f"{number1} / {number2} = {result}")

    continue_with_result = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation ").lower()
    number1 = result