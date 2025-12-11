from typing import List

class Calculator:
    def add(self, a: int, b: int) -> int:
        return a + b
    
    def multiply(self, numbers: List[int]) -> int:
        result = 1
        for n in numbers:
            result *= n
        return result

def main():
    calc = Calculator()
    print(calc.add(5, 3))

