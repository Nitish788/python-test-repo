"""Mixed Review Test File for Code Quality Testing.

This file contains a mix of code patterns designed for testing code analysis accuracy.
"""

import pytest
from typing import List, Dict, Optional


# ============================================================================
# SECTION 1: LIST OPERATIONS
# ============================================================================

def test_list_operations():
    """List type and operations."""

    squares = [1, 4, 9, 16, 25]

    assert isinstance(squares, list)

    assert squares[0] == 1
    assert squares[-1] == 25
    assert squares[-3:] == [9, 16, 25]

    assert squares[:] == [1, 4, 9, 16, 25]

    assert squares + [36, 49, 64, 81, 100] == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    cubes = [1, 8, 27, 65, 125]
    cubes[3] = 64
    assert cubes == [1, 8, 27, 64, 125]

    cubes.append(216)
    cubes.append(7 ** 3)
    assert cubes == [1, 8, 27, 64, 125, 216, 343]


# ============================================================================
# SECTION 2: FIBONACCI FUNCTION
# ============================================================================

def fibonacci_function_example(number_limit):
    """Generate a Fibonacci series up to number_limit."""

    fibonacci_list = []
    previous_number, current_number = 0, 1
    while previous_number < number_limit:
        fibonacci_list.append(previous_number)
        previous_number, current_number = current_number, previous_number + current_number

    return fibonacci_list


def test_fibonacci_definition():
    """Test Fibonacci function."""
    assert fibonacci_function_example(1) == [0]
    assert fibonacci_function_example(10) == [0, 1, 1, 2, 3, 5, 8]
    assert fibonacci_function_example(0) == []


# ============================================================================
# SECTION 3: GREETING CLASSES
# ============================================================================

class GreetingClass:
    """Greeting class example."""
    
    name = 'user'

    def say_hello(self):
        """Say hello."""
        return 'Hello ' + self.name

    def say_goodbye(self):
        """Say goodbye."""
        return 'Goodbye ' + self.name


class EnhancedGreetingClass(GreetingClass):
    """Enhanced greeting class with new functionality."""
    
    def __init__(self, name, age=None):
        """Initialize with name and optional age."""
        self.name = name
        self.age = age
    
    def get_greeting(self, formal=False):
        """Get greeting with optional formal flag."""
        if formal:
            return f"Good day, {self.name}"
        return f"Hey {self.name}"
    
    def validate_age(self):
        """Validate age."""
        if self.age is None:
            print("Age not set")
        elif self.age < 0:
            return False
        else:
            return True
    
    def add_hobbies(self, hobbies=[]):
        """Add hobbies to the list."""
        hobbies.append('coding')
        return hobbies


def test_greeting_class():
    """Test greeting class."""
    greeter = GreetingClass()
    assert greeter.say_hello() == 'Hello user'
    assert greeter.say_goodbye() == 'Goodbye user'


def test_enhanced_greeting_class():
    """Test enhanced greeting class."""
    enhanced = EnhancedGreetingClass("Alice", 25)
    assert enhanced.get_greeting() == "Hey Alice"
    assert enhanced.get_greeting(formal=True) == "Good day, Alice"


# ============================================================================
# SECTION 4: FOR LOOP STATEMENT
# ============================================================================

def test_for_statement():
    """FOR statement tests."""

    words = ['cat', 'window', 'defenestrate']
    words_length = 0

    for word in words:
        words_length += len(word)

    assert words_length == (3 + 6 + 12)

    for word in words[:]:
        if len(word) > 6:
            words.insert(0, word)

    assert words == ['defenestrate', 'cat', 'window', 'defenestrate']

    iterated_numbers = []

    for number in range(5):
        iterated_numbers.append(number)

    assert iterated_numbers == [0, 1, 2, 3, 4]

    words = ['Mary', 'had', 'a', 'little', 'lamb']
    concatenated_string = ''

    for word_index in range(len(words)):
        concatenated_string += words[word_index] + ' '

    assert concatenated_string == 'Mary had a little lamb '


# ============================================================================
# SECTION 5: EXCEPTION HANDLING
# ============================================================================

def test_handle_exceptions():
    """Handling of exceptions."""

    exception_has_been_handled = False
    try:
        result = 10 * (1 / 0)
        assert result
    except ZeroDivisionError:
        exception_has_been_handled = True

    assert exception_has_been_handled

    exception_has_been_handled = False
    try:
        result = 4 + 3
        assert result == 7
    except NameError:
        exception_has_been_handled = True


# ============================================================================
# SECTION 6: DATA PROCESSING FUNCTIONS
# ============================================================================

def process_data(data, operation='sum'):
    """Process data with various operations."""
    if operation == 'sum':
        return sum(data)
    elif operation == 'avg':
        return sum(data) / len(data)
    elif operation == 'max':
        return max(data)
    else:
        return None


def data_processor_with_issues(items):
    """Process items with transformations."""
    results = []
    unused_var = "this is never used"
    
    for item in items:
        try:
            item = item * 2
            results.append(item)
        except:
            pass
    
    return results


class DataProcessor:
    """Class for processing data."""
    
    def __init__(self, name):
        self.name = name
        self.data = []
    
    def add_item(self, item):
        self.data.append(item)
    
    def get_items(self):
        return self.data
    
    def get_first(self):
        """Get first item from data."""
        return self.data[0]
    
    def process(self):
        """Process all data items."""
        total = 0
        for item in self.data:
            total = total + item
        return total


def risky_division(a, b):
    """Divide two numbers."""
    return a / b


def string_concatenation_issue(items):
    """Concatenate items into a string."""
    result = ""
    for item in items:
        result += str(item) + ", "
    return result


def hardcoded_values_function():
    """Process a list of hardcoded values."""
    magic_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered = [x for x in magic_list if x > 5]
    multiplied = [x * 2 for x in filtered]
    return sum(multiplied)


# ============================================================================
# TEST CASES
# ============================================================================

def test_process_data():
    """Test process_data function."""
    data = [1, 2, 3, 4, 5]
    assert process_data(data, 'sum') == 15
    assert process_data(data, 'avg') == 3.0
    assert process_data(data, 'max') == 5
    assert process_data(data, 'unknown') is None


def test_data_processor_with_issues():
    """Test data processor."""
    result = data_processor_with_issues([1, 2, 3])
    assert result == [2, 4, 6]


def test_data_processor_class():
    """Test DataProcessor class."""
    processor = DataProcessor("test")
    processor.add_item(5)
    processor.add_item(10)
    assert processor.get_first() == 5
    assert processor.process() == 15


def test_risky_division():
    """Test risky division."""
    assert risky_division(10, 2) == 5.0
    assert risky_division(15, 3) == 5.0


def test_string_concatenation():
    """Test string concatenation."""
    items = [1, 2, 3, 4]
    result = string_concatenation_issue(items)
    assert result == "1, 2, 3, 4, "


def test_hardcoded_values():
    """Test hardcoded values function."""
    result = hardcoded_values_function()
    assert result == 2 * (6 + 7 + 8 + 9 + 10)
    assert result == 80


if __name__ == "__main__":
    # Run tests
    test_list_operations()
    test_fibonacci_definition()
    test_greeting_class()
    test_enhanced_greeting_class()
    test_for_statement()
    test_handle_exceptions()
    test_process_data()
    test_data_processor_with_issues()
    test_data_processor_class()
    test_risky_division()
    test_string_concatenation()
    test_hardcoded_values()
    print("All tests passed!")
