# C-Python-Calculator
Command-line calculator with C backend and Python interface

# C-Python-Calculator
Command-line calculator with C backend and Python interface


### Complete `README.md`

```markdown
# C-Python Calculator

A command-line calculator with core arithmetic logic implemented in C and exposed through a Python interface. This project demonstrates the integration of C extensions with Python, packaged as a distributable Python module.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [CI/CD Workflow](#ci-cd-workflow)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Features
- Performs addition, subtraction, multiplication, and division.
- Offers both interactive and command-line interface (CLI) modes.
- Utilizes a C-based backend for performance, wrapped in a Python API.
- Packaged as a Python module for easy import and distribution.

## Prerequisites
Before running the project, install the following on your Windows system:

1. **Python 3.10**:
   - Download from [python.org](https://www.python.org/downloads/release/python-3100/) or use your package manager.
   - Verify with: `python --version` (should output `Python 3.10.x`).
   - Ensure `pip` is included (verify with `pip --version`).

2. **MinGW (Minimalist GNU for Windows)**:
   - Required to compile the C extension.
   - Install via MSYS2:
     - Download MSYS2 from [msys2.org](https://www.msys2.org/).
     - Open MSYS2 MinGW 64-bit terminal and run: `pacman -S mingw-w64-x86_64-gcc`.
   - Add the MinGW `bin` directory (e.g., `C:\msys64\mingw64\bin`) to your system PATH.



## Installation

### Clone the Repository
1. Clone the repository to your local machine:
   ```
   git clone https://github.com/marcilino-adel/C-Python-Calculator.git
   cd C-Python-Calculator
   ```

### Build the C Extension
The project includes a C file (`src/c/calculator.c`) that must be compiled into a Python extension (`calculator.pyd`).

1. **Replace Directories**:
   - The build commands below use specific paths based on the developer's setup. Replace these with your own paths:
     - Replace `C:\Users\Marcilino\AppData\Local\Programs\Python\Python310` with the path to your Python 3.10 installation (e.g., `C:\Users\YourUsername\AppData\Local\Programs\Python\Python310`).
     - Replace `C:\Program Files\JetBrains\CLion 2025.1\bin\mingw\bin\gcc.exe` with the path to your MinGW `gcc.exe` (e.g., `C:\msys64\mingw64\bin\gcc.exe`).

2. **Compile and Link**:
   - Open a Command Prompt or PowerShell and navigate to the project directory.
   - Run the following commands to build the C extension:
     ```
     "C:\Users\Marcilino\AppData\Local\Programs\Python\Python310\python.exe" -m pip install --upgrade pip
     "C:\Users\Marcilino\AppData\Local\Programs\Python\Python310\python.exe" -m pip install build
     "C:\Users\Marcilino\AppData\Local\Programs\Python\Python310\python.exe" -m pip install numpy
     "C:\Program Files\JetBrains\CLion 2025.1\bin\mingw\bin\gcc.exe" -Wall -Wextra -fPIC -IC:\Users\Marcilino\AppData\Local\Programs\Python\Python310\include -c src/c/calculator.c -o src/c/calculator.o
     "C:\Program Files\JetBrains\CLion 2025.1\bin\mingw\bin\gcc.exe" -shared -o calculator.pyd src/c/calculator.o -LC:\Users\Marcilino\AppData\Local\Programs\Python\Python310\libs -lpython310
     ```

3. **Build the Package**:
   - Generate the distributable files:
     ```
     "C:\Users\Marcilino\AppData\Local\Programs\Python\Python310\python.exe" -m build
     ```
   - This creates `dist/c_python_calculator-1.0.0.tar.gz` and `dist/c_python_calculator-1.0.0-py3-none-any.whl`.

4. **Install the Package**:
   - Install the built package into your Python environment:
     ```
     "C:\Users\Marcilino\AppData\Local\Programs\Python\Python310\python.exe" -m pip install dist/c_python_calculator-1.0.0.tar.gz
     ```

### Verify Installation
- Confirm the package is installed:
  ```
  "C:\Users\Marcilino\AppData\Local\Programs\Python\Python310\python.exe" -m pip show c_python_calculator
  ```
- Check that the `Location` field points to your Python `site-packages` directory (e.g., `C:\Users\YourUsername\AppData\Local\Programs\Python\Python310\lib\site-packages`).

## Usage

### Command-Line Interface (CLI)
- Run the calculator with command-line arguments:
  ```
  "C:\Users\Marcilino\AppData\Local\Programs\Python\Python310\python.exe" -m c_python_calculator 5 + 3
  ```
  - Output: `5 + 3 = 8.0`
- Start interactive mode:
  ```
  "C:\Users\Marcilino\AppData\Local\Programs\Python\Python310\python.exe" -m c_python_calculator --interactive
  ```
  - Enter calculations like `5 + 3` and press Enter. Type `quit` to exit.

### Python Module
- Use the `Calculator` class in your Python scripts:
  - Create a file named `test.py`:
    ```python
    from c_python_calculator import Calculator

    calc = Calculator()
    print(calc.add(2, 3))  # Output: 5.0
    print(calc.subtract(5, 2))  # Output: 3.0
    ```
  - Run it:
    ```
    "C:\Users\Marcilino\AppData\Local\Programs\Python\Python310\python.exe" test.py
    ```

## Testing
- The project includes a `test.py` file to verify functionality.
- After installation, run:
  ```
  "C:\Users\Marcilino\AppData\Local\Programs\Python\Python310\python.exe" test.py
  ```
- Expected output:
  ```
  Import successful
  Add: 5.0
  Subtract: 3.0
  ```
- Ensure `calculator.pyd` is built and installed correctly before testing.

## CI/CD Workflow
- The project uses GitHub Actions for automated processes.
- **Workflow File**: `.github/workflows/ci-cd.yml`.
- **Automated Tasks**:
  - Builds the C extension and package.
  - Runs `test.py` to validate functionality.
  - Performs code scanning with CodeQL for Python and C code.
- **Optional Deployment**: Tag a release (e.g., `git tag v1.0.0` and `git push origin v1.0.0`) to upload `dist` files to GitHub Releases. No manual setup is required; it runs on push/pull requests to `main`.

## Project Structure
```
C-Python-Calculator/
├── src/
│   ├── c/
│   │   ├── calculator.c    # C source code for the calculator
│   │   └── calculator.h    # C header file (if any)
│   ├── python/
│   │   ├── __init__.py     # Package initialization
│   │   └── interface.py    # Python interface to the C extension
├── test.py                 # Test script
├── setup.py                # Setuptools configuration
├── pyproject.toml          # Project metadata
├── MANIFEST.in             # Files to include in the package
├── .gitignore              # Ignored files (e.g., dist, calculator.pyd)
├── .github/workflows/      # CI/CD configuration
│   └── ci-cd.yml
├── README.md               # This file
└── LICENSE                 # License file
```

## Troubleshooting
- **"No module named c_python_calculator"**:
  - Ensure the package is installed in the Python environment running the script. Use the correct Python executable path (e.g., replace with your path).
- **GCC Compilation Errors**:
  - Verify MinGW is in your PATH.
  - Ensure the include (`-I`) and library (`-L`) paths match your Python installation.
- **Build Fails**:
  - Check that `calculator.c` compiles without errors. Adjust paths in the GCC commands.
- **Import Errors in `interface.py`**:
  - Confirm `calculator.pyd` is in the project root before building and in `site-packages/c_python_calculator` after installation.

## Contributing
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-branch`.
3. Commit changes: `git commit -m "Add feature"`.
4. Push and open a pull request.

## License
- [MIT License](LICENSE) - Free to use, modify, and distribute.
```