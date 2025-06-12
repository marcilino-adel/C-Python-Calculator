cmake_minimum_required(VERSION 3.21)
project(CPythonCalculator C)

set(CMAKE_C_STANDARD 11)

# Add the calculator library
add_library(calculator STATIC
        src/c/calculator.c
)

target_include_directories(calculator PUBLIC
        ${PROJECT_SOURCE_DIR}/src/c
)

# Add the C unit test executable
add_executable(test_calculator
        tests/test_calculator.c
)

target_link_libraries(test_calculator calculator)
