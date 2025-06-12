import calculator
print("2 + 3 =", calculator.add(2, 3))
from c_python_calculator import Calculator
calc = Calculator()
print("Import successful")
print(f"Add: {calc.add(2, 3)}")  # Should output 5.0
print(f"Subtract: {calc.subtract(5, 2)}")  # Should output 3.0
