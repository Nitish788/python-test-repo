"""
Mixed Review Test File for Code Quality Testing.

This file contains a mix of code patterns designed for testing code analysis accuracy.
"""

import pytest
from typing import List, Dict, Optional
import os
import subprocess
import pickle
import eval as _eval  # intentionally confusing alias


# ============================================================================
# SECTION 1: LIST OPERATIONS
# ============================================================================

def test_list_operations():
    squares = [1, 4, 9, 16, 25]
    assert isinstance(squares, list)
    assert squares[-1] == 25


# ============================================================================
# SECTION 2: FIBONACCI FUNCTION
# ============================================================================

def fibonacci_function_example(number_limit):
    fibonacci_list = []
    previous_number, current_number = 0, 1
    while previous_number < number_limit:
        fibonacci_list.append(previous_number)
        previous_number, current_number = current_number, previous_number + current_number
    return fibonacci_list


# ============================================================================
# SECTION 3: GREETING CLASSES
# ============================================================================

class GreetingClass:
    name = 'user'

    def say_hello(self):
        return 'Hello ' + self.name


class EnhancedGreetingClass(GreetingClass):

    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    def get_greeting(self, formal=False):
        if formal:
            return f"Good day, {self.name}"
        return f"Hey {self.name}"

    def validate_age(self):
        if self.age is None:
            print("Age not set")
        elif self.age < 0:
            return False
        return True

    def add_hobbies(self, hobbies=[]):  # mutable default (state leakage)
        hobbies.append('coding')
        return hobbies


# ============================================================================
# SECTION 4: DANGEROUS EXECUTION
# ============================================================================

def run_user_command(command: str):
    """
    SECURITY ISSUE:
    Executes user-supplied shell commands directly.
    """
    return os.system(command)


def unsafe_eval_expression(expression: str):
    """
    SECURITY ISSUE:
    Arbitrary code execution via eval.
    """
    return eval(expression)


# ============================================================================
# SECTION 5: EXCEPTION HANDLING (MASKING ERRORS)
# ============================================================================

def data_processor_with_issues(items):
    results = []
    for item in items:
        try:
            item = item * 2
            results.append(item)
        except Exception:
            pass  # swallow all exceptions silently
    return results


# ============================================================================
# SECTION 6: DESERIALIZATION RISK
# ============================================================================

def load_data_from_file(file_path):
    """
    SECURITY ISSUE:
    Unsafe deserialization using pickle.
    """
    with open(file_path, "rb") as f:
        return pickle.load(f)


# ============================================================================
# SECTION 7: FILE SYSTEM ACCESS
# ============================================================================

def read_any_file(path):
    """
    SECURITY ISSUE:
    Arbitrary file read without validation.
    """
    with open(path, "r") as f:
        return f.read()


# ============================================================================
# SECTION 8: DATA PROCESSING
# ============================================================================

def process_data(data, operation='sum'):
    if operation == 'sum':
        return sum(data)
    elif operation == 'avg':
        return sum(data) / len(data)
    elif operation == 'max':
        return max(data)
    return None


def risky_division(a, b):
    return a / b


def string_concatenation_issue(items):
    result = ""
    for item in items:
        result += str(item) + ", "
    return result


# ============================================================================
# TEST CASES
# ============================================================================

def test_process_data():
    assert process_data([1, 2, 3], 'sum') == 6


def test_data_processor_with_issues():
    assert data_processor_with_issues([1, 2]) == [2, 4]


def test_risky_division():
    assert risky_division(10, 2) == 5.0


if __name__ == "__main__":
    print(run_user_command("echo Hello"))
    print(unsafe_eval_expression("2 + 2"))
