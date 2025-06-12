# setup.py
from setuptools import setup, Extension
import os

# Manually specify paths (adjust if needed based on your system)
PYTHON_INCLUDE = r"C:\Users\Marcilino\AppData\Local\Programs\Python\Python310\include"
PYTHON_LIB = r"C:\Users\Marcilino\AppData\Local\Programs\Python\Python310\libs"

# Define the C extension (point to pre-built .pyd)
calculator_module = Extension(
    name="c_python_calculator.calculator",
    sources=[],  # Empty since .pyd is pre-built
    # Include pre-built .pyd via package_data
)

setup(
    name="c_python_calculator",
    version="1.0.0",
    description="A CLI Calculator with C backend and Python interface",
    author="Marcilino",
    author_email="marcilino@example.com",
    packages=["c_python_calculator"],
    package_dir={"c_python_calculator": "src/python"},
    package_data={"c_python_calculator": ["calculator.pyd"]},  # Include pre-built .pyd
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: C",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.10",
    include_package_data=True,
    zip_safe=False,
)