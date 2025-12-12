"""
Python Language Constructs - A comprehensive guide to Python constructs.

This module demonstrates various language constructs in Python including functions,
classes, decorators, generators, context managers, comprehensions, and more.
Each construct includes detailed examples with 5+ lines of meaningful code.
"""

import time
import functools
from typing import List, Dict, Generator, Iterator, Any, Optional, Union
from abc import ABC, abstractmethod
from contextlib import contextmanager
from dataclasses import dataclass
from enum import Enum
import logging

# ============================================================================
# 1. FUNCTIONS - BASIC, DEFAULT ARGUMENTS, *ARGS, **KWARGS
# ============================================================================

def greet(name, greeting="Hello", exclamation_marks=1):
    """
    Basic function with default arguments.
    
    Args:
        name: Name of the person to greet
        greeting: The greeting message (default: "Hello")
        exclamation_marks: Number of exclamation marks (default: 1)
        
    Returns:
        str: Formatted greeting message
    """
    return f"{greeting}, {name}{'!' * exclamation_marks}"

def sum_numbers(*args):
    """
    Function that accepts variable number of positional arguments.
    
    Args:
        *args: Variable number of numeric arguments
        
    Returns:
        Union[int, float]: Sum of all arguments
        
    Example:
        >>> sum_numbers(1, 2, 3, 4, 5)
        15
    """
    total = 0
    for number in args:
        total += number
    return total

def create_dict(**kwargs):
    """
    Function that accepts variable keyword arguments.
    
    Args:
        **kwargs: Variable number of keyword arguments
        
    Returns:
        dict: Dictionary created from keyword arguments
        
    Example:
        >>> create_dict(name="John", age=30, city="NYC")
        {'name': 'John', 'age': 30, 'city': 'NYC'}
    """
    result = {}
    for key, value in kwargs.items():
        result[key] = value
    return result

def flexible_function(a, b, *args, flag=False, **kwargs):
    """
    Function combining positional, *args, keyword-only, and **kwargs.
    
    Args:
        a: First required argument
        b: Second required argument
        *args: Additional positional arguments
        flag: Keyword-only argument with default
        **kwargs: Additional keyword arguments
        
    Returns:
        dict: Dictionary with all arguments
    """
    return {
        'a': a,
        'b': b,
        'args': args,
        'flag': flag,
        'kwargs': kwargs
    }

# ============================================================================
# 2. LAMBDA FUNCTIONS (ANONYMOUS FUNCTIONS)
# ============================================================================

# Simple lambda
square = lambda x: x ** 2

# Lambda with multiple arguments
add = lambda x, y: x + y

# Lambda with conditional
absolute_value = lambda x: x if x >= 0 else -x

# Lambda used with built-in functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
squared_numbers = list(map(lambda x: x ** 2, numbers))
sorted_descending = sorted(numbers, key=lambda x: -x)

# Lambda in dictionary for lookup
operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y,
    'divide': lambda x, y: x / y if y != 0 else None,
}

# ============================================================================
# 3. DECORATORS - FUNCTION DECORATORS
# ============================================================================

def timing_decorator(func):
    """
    Decorator that measures function execution time.
    
    Args:
        func: Function to be decorated
        
    Returns:
        function: Wrapped function with timing functionality
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def retry_decorator(max_retries=3, delay=1):
    """
    Decorator that retries function on failure.
    
    Args:
        max_retries: Maximum number of retry attempts
        delay: Delay between retries in seconds
        
    Returns:
        function: Decorator function
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise
                    time.sleep(delay)
                    print(f"Attempt {attempt + 1} failed, retrying...")
            return None
        return wrapper
    return decorator

def logging_decorator(func):
    """
    Decorator that logs function calls with arguments.
    
    Args:
        func: Function to be decorated
        
    Returns:
        function: Wrapped function with logging
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

def validation_decorator(func):
    """
    Decorator that validates function arguments.
    
    Args:
        func: Function to be decorated
        
    Returns:
        function: Wrapped function with validation
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not args:
            raise ValueError("Function requires at least one argument")
        if any(arg is None for arg in args):
            raise ValueError("Arguments cannot be None")
        return func(*args, **kwargs)
    return wrapper

# Apply decorators to functions
@timing_decorator
@logging_decorator
def slow_function(n):
    """Function decorated with timing and logging."""
    time.sleep(0.1)
    return sum(range(n))

@retry_decorator(max_retries=2, delay=0.5)
def unreliable_function():
    """Function that may fail and will be retried."""
    import random
    if random.random() < 0.7:
        raise Exception("Random failure")
    return "Success"

# ============================================================================
# 4. CLASSES - BASIC, INHERITANCE, PROPERTIES, METHODS
# ============================================================================

class Animal:
    """Base class for animals with common attributes and methods."""
    
    def __init__(self, name, age):
        """
        Initialize an animal.
        
        Args:
            name: Name of the animal
            age: Age of the animal
        """
        self.name = name
        self.age = age
        self._energy = 100
    
    def speak(self):
        """Make the animal speak."""
        raise NotImplementedError("Subclasses must implement speak method")
    
    def age_one_year(self):
        """Increase the animal's age by one year."""
        self.age += 1
        self._energy -= 10
    
    @property
    def energy(self):
        """Get the animal's energy level."""
        return self._energy
    
    @energy.setter
    def energy(self, value):
        """Set the animal's energy level."""
        if 0 <= value <= 100:
            self._energy = value
        else:
            raise ValueError("Energy must be between 0 and 100")
    
    def __str__(self):
        """String representation of the animal."""
        return f"{self.name} (Age: {self.age}, Energy: {self._energy})"
    
    def __repr__(self):
        """Developer-friendly representation."""
        return f"Animal(name='{self.name}', age={self.age})"

class Dog(Animal):
    """Dog class inheriting from Animal."""
    
    def __init__(self, name, age, breed):
        """
        Initialize a dog.
        
        Args:
            name: Name of the dog
            age: Age of the dog
            breed: Breed of the dog
        """
        super().__init__(name, age)
        self.breed = breed
    
    def speak(self):
        """Make the dog bark."""
        return f"{self.name} says: Woof! Woof!"
    
    def fetch(self, item):
        """Dog fetches an item."""
        if self._energy > 10:
            self._energy -= 15
            return f"{self.name} fetched the {item}"
        else:
            return f"{self.name} is too tired to fetch"

class Cat(Animal):
    """Cat class inheriting from Animal."""
    
    def __init__(self, name, age, indoor=True):
        """
        Initialize a cat.
        
        Args:
            name: Name of the cat
            age: Age of the cat
            indoor: Whether the cat is indoor or outdoor
        """
        super().__init__(name, age)
        self.indoor = indoor
    
    def speak(self):
        """Make the cat meow."""
        return f"{self.name} says: Meow! Meow!"
    
    def scratch(self, item):
        """Cat scratches an item."""
        return f"{self.name} scratched the {item}"

# ============================================================================
# 5. ABSTRACT CLASSES AND ABSTRACT METHODS
# ============================================================================

class Shape(ABC):
    """Abstract base class for shapes."""
    
    def __init__(self, color):
        """
        Initialize shape with color.
        
        Args:
            color: Color of the shape
        """
        self.color = color
    
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass
    
    def describe(self):
        """Describe the shape."""
        return f"A {self.color} shape"

class Circle(Shape):
    """Circle shape implementation."""
    
    def __init__(self, color, radius):
        """Initialize a circle."""
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        """Calculate circle area."""
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        """Calculate circle circumference."""
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    """Rectangle shape implementation."""
    
    def __init__(self, color, width, height):
        """Initialize a rectangle."""
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate rectangle area."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate rectangle perimeter."""
        return 2 * (self.width + self.height)

# ============================================================================
# 6. DATA CLASSES
# ============================================================================

@dataclass
class Person:
    """Person represented as a data class."""
    name: str
    age: int
    email: str
    city: str = "Unknown"
    
    def birthday(self):
        """Increment age by one year."""
        self.age += 1
    
    def __str__(self):
        """String representation."""
        return f"{self.name}, {self.age} years old, {self.email}"

@dataclass
class Point:
    """Represents a 2D point."""
    x: float
    y: float
    
    def distance_from_origin(self):
        """Calculate distance from origin."""
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def move(self, dx, dy):
        """Move the point by dx, dy."""
        self.x += dx
        self.y += dy

# ============================================================================
# 7. ENUMS (ENUMERATION)
# ============================================================================

class Status(Enum):
    """Status enumeration."""
    PENDING = "pending"
    ACTIVE = "active"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

class Priority(Enum):
    """Priority levels."""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

class Color(Enum):
    """Color enumeration with methods."""
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    
    def hex_code(self):
        """Convert RGB to hex code."""
        r, g, b = self.value
        return f"#{r:02x}{g:02x}{b:02x}"

# ============================================================================
# 8. GENERATORS AND GENERATOR FUNCTIONS
# ============================================================================

def fibonacci_generator(n: int) -> Generator[int, None, None]:
    """
    Generate fibonacci numbers up to n.
    
    Args:
        n: Maximum number to generate up to
        
    Yields:
        int: Next fibonacci number
    """
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

def count_up(start: int = 0, end: int = 10) -> Generator[int, None, None]:
    """
    Generate numbers from start to end.
    
    Args:
        start: Starting number
        end: Ending number
        
    Yields:
        int: Next number in range
    """
    current = start
    while current <= end:
        yield current
        current += 1

def read_large_file(file_path: str, chunk_size: int = 1024):
    """
    Generator for reading large files in chunks.
    
    Args:
        file_path: Path to the file
        chunk_size: Size of each chunk
        
    Yields:
        str: Next chunk of file content
    """
    try:
        with open(file_path, 'r') as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                yield chunk
    except FileNotFoundError:
        print(f"File {file_path} not found")

def infinite_counter(start: int = 0) -> Generator[int, None, None]:
    """
    Generate infinite sequence of numbers.
    
    Args:
        start: Starting number
        
    Yields:
        int: Next number in infinite sequence
    """
    current = start
    while True:
        yield current
        current += 1

# ============================================================================
# 9. LIST, DICT, SET COMPREHENSIONS
# ============================================================================

# List comprehensions
squares = [x**2 for x in range(1, 11)]
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
flattened = [item for sublist in [[1, 2], [3, 4], [5, 6]] for item in sublist]
coordinates = [(x, y) for x in range(3) for y in range(3)]

# Dictionary comprehensions
squares_dict = {x: x**2 for x in range(1, 6)}
word_lengths = {word: len(word) for word in ['python', 'java', 'javascript']}
inverted_dict = {v: k for k, v in {'a': 1, 'b': 2, 'c': 3}.items()}
filtered_dict = {k: v for k, v in {'a': 1, 'b': 2, 'c': 3, 'd': 4}.items() if v > 1}

# Set comprehensions
unique_squares = {x**2 for x in range(1, 11)}
odd_numbers_set = {x for x in range(1, 21) if x % 2 != 0}
common_letters = {char for word in ['python', 'programming'] for char in word}

# ============================================================================
# 10. CONTEXT MANAGERS (WITH STATEMENT)
# ============================================================================

@contextmanager
def file_handler(filename: str, mode: str = 'r'):
    """
    Context manager for file handling.
    
    Args:
        filename: Name of the file
        mode: File opening mode
        
    Yields:
        file: File object
    """
    file = None
    try:
        file = open(filename, mode)
        yield file
    except FileNotFoundError:
        print(f"File {filename} not found")
    finally:
        if file:
            file.close()
            print(f"File {filename} closed")

@contextmanager
def timer(name: str = "Operation"):
    """
    Context manager for timing operations.
    
    Args:
        name: Name of the operation
        
    Yields:
        None
    """
    start_time = time.time()
    print(f"Starting {name}...")
    try:
        yield
    finally:
        end_time = time.time()
        print(f"{name} completed in {end_time - start_time:.4f} seconds")

@contextmanager
def database_connection(host: str, user: str, password: str):
    """
    Context manager for database connections.
    
    Args:
        host: Database host
        user: Database user
        password: Database password
        
    Yields:
        str: Connection string
    """
    connection = f"Connected to {host} as {user}"
    print(f"Opening connection: {connection}")
    try:
        yield connection
    finally:
        print(f"Closing connection: {connection}")

# ============================================================================
# 11. ITERATORS
# ============================================================================

class CountUp:
    """Custom iterator that counts up from a start number."""
    
    def __init__(self, max: int):
        """Initialize counter with maximum value."""
        self.max = max
        self.current = 0
    
    def __iter__(self):
        """Return the iterator object."""
        return self
    
    def __next__(self):
        """Return the next value in the iteration."""
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration

class ReverseString:
    """Custom iterator that iterates string in reverse."""
    
    def __init__(self, text: str):
        """Initialize with text."""
        self.text = text
        self.index = len(text)
    
    def __iter__(self):
        """Return the iterator object."""
        return self
    
    def __next__(self):
        """Return the next character in reverse."""
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.text[self.index]

class PowerIterator:
    """Iterator that generates powers of a base."""
    
    def __init__(self, base: float, max_power: int):
        """Initialize with base and max power."""
        self.base = base
        self.max_power = max_power
        self.current_power = 0
    
    def __iter__(self):
        """Return the iterator object."""
        return self
    
    def __next__(self):
        """Return next power."""
        if self.current_power <= self.max_power:
            result = self.base ** self.current_power
            self.current_power += 1
            return result
        else:
            raise StopIteration

# ============================================================================
# 12. CLOSURES
# ============================================================================

def outer_function(x: int):
    """
    Demonstrates closure - function returning a function.
    
    Args:
        x: Value to be captured
        
    Returns:
        function: Inner function that uses x from outer scope
    """
    def inner_function(y: int):
        """Inner function that accesses x from outer scope."""
        return x + y
    return inner_function

def multiplier(factor: int):
    """
    Create a multiplier function with closure.
    
    Args:
        factor: Multiplication factor to be captured
        
    Returns:
        function: Function that multiplies its argument by factor
    """
    def multiply(x: int):
        """Multiply x by the captured factor."""
        return x * factor
    return multiply

def counter():
    """
    Create a counter function with closure over count.
    
    Returns:
        function: Function that increments and returns count
    """
    count = 0
    
    def increment():
        """Increment count and return it."""
        nonlocal count
        count += 1
        return count
    
    return increment

# ============================================================================
# 13. MULTIPLE INHERITANCE
# ============================================================================

class Flyable:
    """Mixin class for flyable objects."""
    
    def fly(self):
        """Method to fly."""
        return f"{self.__class__.__name__} is flying"
    
    def land(self):
        """Method to land."""
        return f"{self.__class__.__name__} has landed"

class Swimmable:
    """Mixin class for swimmable objects."""
    
    def swim(self):
        """Method to swim."""
        return f"{self.__class__.__name__} is swimming"
    
    def dive(self):
        """Method to dive."""
        return f"{self.__class__.__name__} is diving"

class Duck(Flyable, Swimmable):
    """Duck class inheriting from multiple classes."""
    
    def __init__(self, name: str):
        """Initialize a duck."""
        self.name = name
    
    def quack(self):
        """Duck quacks."""
        return f"{self.name} says: Quack!"

# ============================================================================
# 14. STATIC METHODS AND CLASS METHODS
# ============================================================================

class MathUtils:
    """Utility class with static and class methods."""
    
    PI = 3.14159
    instances_created = 0
    
    def __init__(self, value: float):
        """Initialize with a value."""
        self.value = value
        MathUtils.instances_created += 1
    
    @staticmethod
    def is_prime(n: int) -> bool:
        """
        Check if a number is prime (static method).
        
        Args:
            n: Number to check
            
        Returns:
            bool: True if prime, False otherwise
        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    @classmethod
    def from_string(cls, value_str: str):
        """
        Create instance from string (class method).
        
        Args:
            value_str: String representation of value
            
        Returns:
            MathUtils: New instance
        """
        return cls(float(value_str))
    
    @classmethod
    def get_instances_count(cls) -> int:
        """Get number of instances created."""
        return cls.instances_created

# ============================================================================
# 15. HIGHER-ORDER FUNCTIONS
# ============================================================================

def apply_operation(operation, a: float, b: float) -> float:
    """
    Apply an operation to two numbers.
    
    Args:
        operation: Function to apply
        a: First number
        b: Second number
        
    Returns:
        float: Result of operation
    """
    return operation(a, b)

def compose(*functions):
    """
    Compose multiple functions together.
    
    Args:
        *functions: Functions to compose
        
    Returns:
        function: Composed function
    """
    def composed(value):
        """Apply all functions in sequence."""
        result = value
        for func in reversed(functions):
            result = func(result)
        return result
    return composed

def partial_application(func, *partial_args):
    """
    Create a partial application of a function.
    
    Args:
        func: Function to partially apply
        *partial_args: Arguments to pre-fill
        
    Returns:
        function: Function with pre-filled arguments
    """
    def wrapper(*args):
        """Call original function with partial and new arguments."""
        return func(*partial_args, *args)
    return wrapper

# ============================================================================
# MAIN DEMONSTRATION
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("PYTHON LANGUAGE CONSTRUCTS DEMONSTRATION")
    print("=" * 70)
    
    # 1. Functions
    print("\n1. FUNCTIONS:")
    print(f"   {greet('Alice')}")
    print(f"   {greet('Bob', 'Hi', 2)}")
    print(f"   Sum: {sum_numbers(1, 2, 3, 4, 5)}")
    
    # 2. Lambda Functions
    print("\n2. LAMBDA FUNCTIONS:")
    print(f"   Square of 5: {square(5)}")
    print(f"   Add 3 + 7: {add(3, 7)}")
    print(f"   Even numbers: {even_numbers}")
    
    # 3. Decorators
    print("\n3. DECORATORS:")
    result = slow_function(100)
    print(f"   Result: {result}")
    
    # 4. Classes and Inheritance
    print("\n4. CLASSES AND INHERITANCE:")
    dog = Dog("Buddy", 3, "Golden Retriever")
    print(f"   {dog.speak()}")
    print(f"   {dog.fetch('ball')}")
    
    cat = Cat("Whiskers", 2)
    print(f"   {cat.speak()}")
    
    # 5. Abstract Classes
    print("\n5. ABSTRACT CLASSES:")
    circle = Circle("red", 5)
    print(f"   Circle area: {circle.area():.2f}")
    print(f"   Circle perimeter: {circle.perimeter():.2f}")
    
    # 6. Data Classes
    print("\n6. DATA CLASSES:")
    person = Person("John", 30, "john@example.com", "NYC")
    print(f"   {person}")
    person.birthday()
    print(f"   After birthday: {person.age}")
    
    # 7. Enums
    print("\n7. ENUMERATIONS:")
    print(f"   Status: {Status.ACTIVE.value}")
    print(f"   Priority: {Priority.HIGH.value}")
    print(f"   Red hex: {Color.RED.hex_code()}")
    
    # 8. Generators
    print("\n8. GENERATORS:")
    print(f"   Fibonacci (< 50): {list(fibonacci_generator(50))}")
    gen = count_up(1, 5)
    print(f"   Count up (1-5): {list(gen)}")
    
    # 9. Comprehensions
    print("\n9. COMPREHENSIONS:")
    print(f"   Squares: {squares}")
    print(f"   Even numbers: {even_numbers}")
    print(f"   Squares dict: {squares_dict}")
    
    # 10. Context Managers
    print("\n10. CONTEXT MANAGERS:")
    with timer("Sample operation"):
        time.sleep(0.1)
    
    # 11. Iterators
    print("\n11. ITERATORS:")
    counter_iter = CountUp(5)
    print(f"   Count up (1-5): {list(CountUp(5))}")
    reverse_iter = ReverseString("Python")
    print(f"   Reverse 'Python': {''.join(ReverseString('Python'))}")
    
    # 12. Closures
    print("\n12. CLOSURES:")
    adder = outer_function(10)
    print(f"   10 + 5 = {adder(5)}")
    times_three = multiplier(3)
    print(f"   5 * 3 = {times_three(5)}")
    
    count_func = counter()
    print(f"   Counter: {count_func()}, {count_func()}, {count_func()}")
    
    # 13. Multiple Inheritance
    print("\n13. MULTIPLE INHERITANCE:")
    duck = Duck("Donald")
    print(f"   {duck.quack()}")
    print(f"   {duck.fly()}")
    print(f"   {duck.swim()}")
    
    # 14. Static and Class Methods
    print("\n14. STATIC AND CLASS METHODS:")
    print(f"   Is 17 prime? {MathUtils.is_prime(17)}")
    math_obj = MathUtils.from_string("3.14")
    print(f"   Created from string: {math_obj.value}")
    print(f"   Instances created: {MathUtils.get_instances_count()}")
    
    # 15. Higher-Order Functions
    print("\n15. HIGHER-ORDER FUNCTIONS:")
    result = apply_operation(add, 10, 5)
    print(f"   Apply operation (10 + 5): {result}")
    
    double_and_square = compose(square, times_three)
    print(f"   Compose: 2 * 3 squared = {double_and_square(2)}")
    
    print("\n" + "=" * 70)
