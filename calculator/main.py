from calculator import operations

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please try again.")

def main():
    print("Welcome to the CLI Calculator!")
    while True:
        print("\nOptions: add, subtract, multiply, divide, quit")
        operation = input("Choose operation: ").strip().lower()

        if operation == "quit":
            print("Goodbye!")
            break

        if operation not in ["add", "subtract", "multiply", "divide"]:
            print("Invalid operation.")
            continue

        x = get_number("Enter first number: ")
        y = get_number("Enter second number: ")

        try:
            result = getattr(operations, operation)(x, y)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
