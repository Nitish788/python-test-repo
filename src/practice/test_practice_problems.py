"""Practice Problems - Level 1 (Beginner)

Simple coding challenges to practice Python basics.
These problems cover fundamental concepts from the learning modules.

@see: https://www.learnpython.org/en/
"""


def test_practice_string_reverse():
    """Practice: Reverse a string using slicing."""
    text = "hello"
    result = text[::-1]
    assert result == "olleh"


def test_practice_string_uppercase():
    """Practice: Convert string to uppercase and count characters."""
    text = "python"
    result = text.upper()
    length = len(result)
    assert result == "PYTHON"
    assert length == 6


def test_practice_list_sum():
    """Practice: Sum all numbers in a list."""
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    assert total == 15


def test_practice_even_numbers():
    """Practice: Filter even numbers from a list."""
    numbers = [1, 2, 3, 4, 5, 6]
    evens = [n for n in numbers if n % 2 == 0]
    assert evens == [2, 4, 6]


def test_practice_list_max_min():
    """Practice: Find max and min values in a list."""
    numbers = [5, 2, 8, 1, 9, 3]
    max_val = max(numbers)
    min_val = min(numbers)
    assert max_val == 9
    assert min_val == 1


def test_practice_dictionary_access():
    """Practice: Create and access dictionary values."""
    person = {"name": "Alice", "age": 25, "city": "New York"}
    assert person["name"] == "Alice"
    assert person.get("age") == 25
    assert person.get("country", "USA") == "USA"


def test_practice_tuple_unpacking():
    """Practice: Unpack values from a tuple."""
    coordinates = (10, 20, 30)
    x, y, z = coordinates
    assert x == 10
    assert y == 20
    assert z == 30


def test_practice_list_comprehension():
    """Practice: Create new list using list comprehension."""
    numbers = [1, 2, 3, 4, 5]
    squares = [n ** 2 for n in numbers]
    assert squares == [1, 4, 9, 16, 25]


def test_practice_count_vowels():
    """Practice: Count vowels in a string."""
    text = "hello world"
    vowels = "aeiou"
    count = sum(1 for char in text if char.lower() in vowels)
    assert count == 3


def test_practice_remove_duplicates():
    """Practice: Remove duplicates from a list using set."""
    items = [1, 2, 2, 3, 3, 3, 4]
    unique = list(set(items))
    assert len(unique) == 4
    assert set(unique) == {1, 2, 3, 4}
