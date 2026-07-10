

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def pow(num1, num2):
    return num1 ** num2

def mod(num1, num2):
    return num1 % num2

def Calc():
    while(True):
        print("choose your mode")
        print("1. add +")
        print("2. substract -")
        print("3. multiply *")
        print("4. divide /")
        print("5. power **")
        print("6. modulo %")
        print("7. Stop")

        mode = input("enter your mode (1/2/3/4/5/6/7): ")
        if mode not in ("1", "2", "3", "4", "5", "6", "7"):
            print("invalid mode bro..., please try again and add numbers")
            continue

        if mode == "7":
            break

        number1 = float(input("enter your first number: "))
        number2 = float(input("enter your second number: "))


        if mode == "1":
            result = add(num1=number1, num2=number2)
        elif mode == "2":
            result = sub(num1=number1, num2=number2)
        elif mode == "3":
            result = mul(num1=number1, num2=number2)
        elif mode == "4":
            if number2 == 0:
                print("error !! you cannot divide by zero idiot")
            else:
                result = div(num1=number1, num2=number2)

        elif mode == "5":
            result = pow(num1=number1, num2=number2)
        elif mode == "6":
            result = mod(num1=number1, num2=number2)

        answer = input("do you want to continue? (y/n): ")

        if answer == "n":
            break
        if answer == "y":
            continue
Calc()