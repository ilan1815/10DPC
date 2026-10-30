#simple calculator using function
def calculate(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "sub":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "div":
        if num2 == 0:
            return "Error : 2 nd num is not in Zero"
        return num1 / num2
    else:
        return "Invalid operations"


def main():
    print("----Simple Calculator----")

    while True:
        try:
            val1 = float(input("\nEnter first number: "))
        except ValueError:
            print("enter the valid number")
            continue

        print("\nAvailable Operations")
        print("+ : add")
        print("- : sub")
        print("* : multiply")
        print("/ : div")
        print("q : quit")

        choice = input("choose an operation (+,-,*,/,q): ").strip().lower()

        operation_map = {"+": "add", "-": "sub", "*": "multiply", "/": "div"}

        if choice == "q":
            print("Exiting Calculator")
            break
        elif choice in operation_map:
            op = operation_map[choice]
        else:
            print("Invalid Operation")
            continue

        try:
            val2 = float(input("enter second number: "))
        except ValueError:
            print("invalid input")
            continue

        result = calculate(val1, val2, op)
        print(f"\nresult: {result}")


if __name__ == "__main__":
    main()
