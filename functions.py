import cmath

def add(a, b):
    """Add two numbers."""
    return a + b

def minus(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b    

def root(a):
    """Return the square root of a. Supports complex results for negative inputs."""
    return cmath.sqrt(a)

def square(a):
    return a**2
    
def divide(a, b):
    if b==0:
        return "0으로 나눌 수 없음."
    return a / b 
    