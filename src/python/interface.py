"""
Python interface for the C-based calculator.

This module provides both a Python API and CLI functionality for the calculator.
"""

import sys
import argparse

try:
    import calculator  # This is the C extension module
except ImportError as e:
    print(f"Error: Could not import calculator module: {e}")
    print("Make sure the calculator.pyd file has been built successfully.")
    sys.exit(1)


class Calculator:
    """
    A calculator class that provides a Python interface to C-implemented operations.

    This class wraps the C extension module to provide a clean Python API.
    """

    @staticmethod
    def add(a, b):
        """
        Add two numbers.

        Args:
            a (float): First number
            b (float): Second number

        Returns:
            float: Sum of a and b
        """
        return calculator.add(float(a), float(b))

    @staticmethod
    def subtract(a, b):
        """
        Subtract second number from first number.

        Args:
            a (float): First number
            b (float): Second number

        Returns:
            float: Difference of a and b
        """
        return calculator.subtract(float(a), float(b))

    @staticmethod
    def multiply(a, b):
        """
        Multiply two numbers.

        Args:
            a (float): First number
            b (float): Second number

        Returns:
            float: Product of a and b
        """
        return calculator.multiply(float(a), float(b))

    @staticmethod
    def divide(a, b):
        """
        Divide first number by second number.

        Args:
            a (float): Dividend
            b (float): Divisor

        Returns:
            float: Quotient of a and b

        Raises:
            ZeroDivisionError: If b is zero
        """
        return calculator.divide(float(a), float(b))

    @staticmethod
    def calculate(operation, a, b):
        """
        Perform calculation based on operation string.

        Args:
            operation (str): Operation to perform (+, -, *, /)
            a (float): First number
            b (float): Second number

        Returns:
            float: Result of the operation

        Raises:
            ValueError: If operation is not supported
        """
        operations = {
            '+': Calculator.add,
            'add': Calculator.add,
            '-': Calculator.subtract,
            'subtract': Calculator.subtract,
            '*': Calculator.multiply,
            'multiply': Calculator.multiply,
            '/': Calculator.divide,
            'divide': Calculator.divide
        }

        if operation not in operations:
            raise ValueError(f"Unsupported operation: {operation}")

        return operations[operation](a, b)


def interactive_mode():
    """Run the calculator in interactive mode."""
    print("=== C-Python Calculator ===")
    print("Enter calculations in the format: <number> <operation> <number>")
    print("Supported operations: +, -, *, /")
    print("Type 'quit' or 'exit' to quit")
    print()

    calc = Calculator()

    while True:
        try:
            user_input = input(">>> ").strip()

            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break

            if not user_input:
                continue

            # Parse input like "5 + 3"
            parts = user_input.split()
            if len(parts) != 3:
                print("Error: Please enter in format: <number> <operation> <number>")
                continue

            try:
                a = float(parts[0])
                operation = parts[1]
                b = float(parts[2])
            except ValueError:
                print("Error: Invalid number format")
                continue

            result = calc.calculate(operation, a, b)
            print(f"Result: {result}")

        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


def cli_mode():
    """Run the calculator in command-line mode."""
    parser = argparse.ArgumentParser(
        description="C-Python Calculator - Perform basic arithmetic operations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m src.python.interface 5 + 3
  python -m src.python.interface 10 / 2
  python -m src.python.interface --interactive
        """
    )

    parser.add_argument('a', nargs='?', type=float, help='First number')
    parser.add_argument('operation', nargs='?', choices=['+', '-', '*', '/', 'add', 'subtract', 'multiply', 'divide'],
                        help='Operation to perform')
    parser.add_argument('b', nargs='?', type=float, help='Second number')
    parser.add_argument('-i', '--interactive', action='store_true',
                        help='Run in interactive mode')

    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
        return

    if args.a is None or args.operation is None or args.b is None:
        parser.print_help()
        return

    calc = Calculator()

    try:
        result = calc.calculate(args.operation, args.a, args.b)
        print(f"{args.a} {args.operation} {args.b} = {result}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    cli_mode()