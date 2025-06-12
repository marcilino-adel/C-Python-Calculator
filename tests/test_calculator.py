"""
Unit tests for the Python interface of the C-Python Calculator.

Tests both the C extension module directly and the Python wrapper interface.
"""

import pytest
import sys
import os

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

try:
    import calculator  # C extension module
    from python.interface import Calculator
    CALCULATOR_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Could not import calculator modules: {e}")
    print("Make sure the calculator.pyd file has been built successfully.")
    CALCULATOR_AVAILABLE = False


@pytest.mark.skipif(not CALCULATOR_AVAILABLE, reason="Calculator module not available")
class TestCExtensionModule:
    """Test the C extension module directly."""

    def test_add(self):
        """Test addition function."""
        assert calculator.add(2.0, 3.0) == 5.0
        assert calculator.add(-1.0, 1.0) == 0.0
        assert calculator.add(0.0, 0.0) == 0.0
        assert calculator.add(-5.0, -3.0) == -8.0
        assert calculator.add(1.5, 2.5) == 4.0

    def test_subtract(self):
        """Test subtraction function."""
        assert calculator.subtract(5.0, 3.0) == 2.0
        assert calculator.subtract(1.0, 1.0) == 0.0
        assert calculator.subtract(-1.0, -1.0) == 0.0
        assert calculator.subtract(0.0, 5.0) == -5.0
        assert calculator.subtract(7.5, 2.5) == 5.0

    def test_multiply(self):
        """Test multiplication function."""
        assert calculator.multiply(2.0, 3.0) == 6.0
        assert calculator.multiply(-2.0, 3.0) == -6.0
        assert calculator.multiply(0.0, 5.0) == 0.0
        assert calculator.multiply(-1.0, -1.0) == 1.0
        assert calculator.multiply(2.5, 4.0) == 10.0

    def test_divide(self):
        """Test division function."""
        assert calculator.divide(6.0, 2.0) == 3.0
        assert calculator.divide(-6.0, 2.0) == -3.0
        assert calculator.divide(0.0, 5.0) == 0.0
        assert calculator.divide(10.0, 4.0) == 2.5
        assert calculator.divide(-8.0, -2.0) == 4.0

    def test_divide_by_zero(self):
        """Test division by zero raises exception."""
        with pytest.raises(ZeroDivisionError):
            calculator.divide(5.0, 0.0)

        with pytest.raises(ZeroDivisionError):
            calculator.divide(-5.0, 0.0)


@pytest.mark.skipif(not CALCULATOR_AVAILABLE, reason="Calculator module not available")
class TestPythonInterface:
    """Test the Python wrapper interface."""

    def setup_method(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_add(self):
        """Test addition through Python interface."""
        assert self.calc.add(2, 3) == 5.0
        assert self.calc.add(-1, 1) == 0.0
        assert self.calc.add(0, 0) == 0.0
        assert self.calc.add(1.5, 2.5) == 4.0

    def test_subtract(self):
        """Test subtraction through Python interface."""
        assert self.calc.subtract(5, 3) == 2.0
        assert self.calc.subtract(1, 1) == 0.0
        assert self.calc.subtract(0, 5) == -5.0
        assert self.calc.subtract(7.5, 2.5) == 5.0

    def test_multiply(self):
        """Test multiplication through Python interface."""
        assert self.calc.multiply(2, 3) == 6.0
        assert self.calc.multiply(-2, 3) == -6.0
        assert self.calc.multiply(0, 5) == 0.0
        assert self.calc.multiply(2.5, 4) == 10.0

    def test_divide(self):
        """Test division through Python interface."""
        assert self.calc.divide(6, 2) == 3.0
        assert self.calc.divide(-6, 2) == -3.0
        assert self.calc.divide(0, 5) == 0.0
        assert self.calc.divide(10, 4) == 2.5

    def test_divide_by_zero(self):
        """Test division by zero through Python interface."""
        with pytest.raises(ZeroDivisionError):
            self.calc.divide(5, 0)

    def test_calculate_method(self):
        """Test the unified calculate method."""
        assert self.calc.calculate('+', 2, 3) == 5.0
        assert self.calc.calculate('add', 2, 3) == 5.0
        assert self.calc.calculate('-', 5, 3) == 2.0
        assert self.calc.calculate('subtract', 5, 3) == 2.0
        assert self.calc.calculate('*', 2, 3) == 6.0
        assert self.calc.calculate('multiply', 2, 3) == 6.0
        assert self.calc.calculate('/', 6, 2) == 3.0
        assert self.calc.calculate('divide', 6, 2) == 3.0

    def test_calculate_invalid_operation(self):
        """Test calculate method with invalid operation."""
        with pytest.raises(ValueError, match="Unsupported operation"):
            self.calc.calculate('%', 5, 2)

        with pytest.raises(ValueError, match="Unsupported operation"):
            self.calc.calculate('invalid', 5, 2)

    def test_type_conversion(self):
        """Test that the interface properly converts types."""
        # Test with integers
        assert self.calc.add(2, 3) == 5.0
        # Test with strings that can be converted to float
        assert self.calc.add("2.5", "3.5") == 6.0
        # Test mixed types
        assert self.calc.multiply(2, 3.5) == 7.0


@pytest.mark.skipif(not CALCULATOR_AVAILABLE, reason="Calculator module not available")
class TestEdgeCases:
    """Test edge cases and error conditions."""

    def setup_method(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_large_numbers(self):
        """Test with large numbers."""
        large_num = 1e10
        assert self.calc.add(large_num, large_num) == 2e10
        assert self.calc.multiply(large_num, 2) == 2e10

    def test_small_numbers(self):
        """Test with very small numbers."""
        small_num = 1e-10
        result = self.calc.add(small_num, small_num)
        assert abs(result - 2e-10) < 1e-15

    def test_negative_numbers(self):
        """Test comprehensive negative number operations."""
        assert self.calc.add(-5, -3) == -8
        assert self.calc.subtract(-5, -3) == -2
        assert self.calc.multiply(-5, -3) == 15
        assert self.calc.divide(-6, -2) == 3

    def test_zero_operations(self):
        """Test operations involving zero."""
        assert self.calc.add(0, 5) == 5
        assert self.calc.subtract(0, 5) == -5
        assert self.calc.multiply(0, 5) == 0
        assert self.calc.divide(0, 5) == 0


if __name__ == "__main__":
    # Run tests with verbose output
    pytest.main([__file__, "-v"])