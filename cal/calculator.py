def pemdas_calculator(expression):
    try:
        # Evaluate the expression using eval
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    while True:
        # Get user input
        expression = input("Enter a mathematical expression (or type 'exit' to quit): ")
        if expression.lower() == 'exit':
            break
        # Calculate and display the result
        result = pemdas_calculator(expression)
        print(f"Result: {result}")
