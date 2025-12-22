    
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def division(x,y):
    if y == 0:
        return "Invalid (division by zero)"
    return x/y

while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Division")
    print("5. Exit")
    

    choice=int(input("enter your choice(1:5):"))
    
    if choice == "5":
        print("Goodbye")
        break
        
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == "1":
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == "2":
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == "3":
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == "4":
        print(num1, "/", num2, "=", division(num1/num2))
    else:
        print("invalid input")