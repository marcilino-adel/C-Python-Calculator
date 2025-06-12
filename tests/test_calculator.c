//
// Created by Marcilino on 6/11/2025.
//
#include <stdio.h>
#include <assert.h>
#include <math.h>
#include "../src/c/calculator.h"

#define EPSILON 1e-9

void test_add() {
    assert(fabs(add(2.0, 3.0) - 5.0) < EPSILON);
    assert(fabs(add(-1.0, 1.0) - 0.0) < EPSILON);
    assert(fabs(add(0.0, 0.0) - 0.0) < EPSILON);
    printf("✓ Addition tests passed\n");
}

void test_subtract() {
    assert(fabs(subtract(5.0, 3.0) - 2.0) < EPSILON);
    assert(fabs(subtract(1.0, 1.0) - 0.0) < EPSILON);
    assert(fabs(subtract(-1.0, -1.0) - 0.0) < EPSILON);
    printf("✓ Subtraction tests passed\n");
}

void test_multiply() {
    assert(fabs(multiply(2.0, 3.0) - 6.0) < EPSILON);
    assert(fabs(multiply(-2.0, 3.0) - (-6.0)) < EPSILON);
    assert(fabs(multiply(0.0, 5.0) - 0.0) < EPSILON);
    printf("✓ Multiplication tests passed\n");
}

void test_divide() {
    assert(fabs(divide(6.0, 2.0) - 3.0) < EPSILON);
    assert(fabs(divide(-6.0, 2.0) - (-3.0)) < EPSILON);
    assert(fabs(divide(0.0, 5.0) - 0.0) < EPSILON);
    printf("✓ Division tests passed\n");
}

int main() {
    printf("Running C unit tests...\n");

    test_add();
    test_subtract();
    test_multiply();
    test_divide();

    printf("All C tests passed! ✓\n");
    return 0;
}