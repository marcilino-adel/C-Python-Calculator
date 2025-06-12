//
// Created by Marcilino on 6/11/2025.
//

#include <Python.h>
#include "calculator.h"

// C implementations (these are needed for C tests)
double add(double a, double b) {
    return a + b;
}

double subtract(double a, double b) {
    return a - b;
}

double multiply(double a, double b) {
    return a * b;
}

double divide(double a, double b) {
    if (b == 0.0) {
        // For C tests, we'll return a special value
        // For Python, we'll set the error below
        return 0.0 / 0.0; // NaN
    }
    return a / b;
}

// Python wrapper functions
static PyObject* py_add(PyObject* self /* unused */, PyObject* args) {
    double a, b;
    if (!PyArg_ParseTuple(args, "dd", &a, &b)) {
        return NULL;
    }
    return PyFloat_FromDouble(add(a, b));
}

static PyObject* py_subtract(PyObject* self, PyObject* args) {
    double a, b;
    if (!PyArg_ParseTuple(args, "dd", &a, &b)) {
        return NULL;
    }
    return PyFloat_FromDouble(subtract(a, b));
}

static PyObject* py_multiply(PyObject* self, PyObject* args) {
    double a, b;
    if (!PyArg_ParseTuple(args, "dd", &a, &b)) {
        return NULL;
    }
    return PyFloat_FromDouble(multiply(a, b));
}

static PyObject* py_divide(PyObject* self, PyObject* args) {
    double a, b;
    if (!PyArg_ParseTuple(args, "dd", &a, &b)) {
        return NULL;
    }
    if (b == 0.0) {
        PyErr_SetString(PyExc_ZeroDivisionError, "Division by zero");
        return NULL;
    }
    return PyFloat_FromDouble(divide(a, b));
}

// Method definitions
static PyMethodDef calculator_methods[] = {
    {"add", py_add, METH_VARARGS, "Add two numbers"},
    {"subtract", py_subtract, METH_VARARGS, "Subtract two numbers"},
    {"multiply", py_multiply, METH_VARARGS, "Multiply two numbers"},
    {"divide", py_divide, METH_VARARGS, "Divide two numbers"},
    {NULL, NULL, 0, NULL}
};

// Module definition
static struct PyModuleDef calculator_module = {
    PyModuleDef_HEAD_INIT,
    "calculator",
    "A simple calculator module",
    -1,
    calculator_methods
};

// Module initialization
PyMODINIT_FUNC PyInit_calculator(void) {
    return PyModule_Create(&calculator_module);
}