"""
C-Python Calculator Package

A command-line calculator with core logic implemented in C and exposed through Python.
Supports basic arithmetic operations: addition, subtraction, multiplication, and division.
"""

from .interface import Calculator

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

# Make Calculator available at package level
__all__ = ["Calculator"]