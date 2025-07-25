from mcp.server.fastmcp import FastMCP
import math
import numpy as np
import sympy as sp
from typing import List

mcp = FastMCP("Math")

# 基本数学运算
@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers"""
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract two numbers"""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@mcp.tool()
def power(base: float, exponent: float) -> float:
    """Raise a number to the power of another"""
    return base ** exponent

@mcp.tool()
def nth_root(x: float, n: float) -> float:
    """Return the n-th root of a number x (e.g., n=2 means square root)"""
    if n == 0:
        raise ValueError("Root order n cannot be zero")
    if x < 0 and n % 2 == 0:
        raise ValueError("Cannot take even root of negative number (result would be complex)")
    return x ** (1 / n)

@mcp.tool()
def log(x: float, base: float = math.e) -> float:
    """Compute logarithm of x with optional base (default: natural log)"""
    if x <= 0:
        raise ValueError("Logarithm only defined for positive numbers")
    return math.log(x, base)

@mcp.tool()
def sin(x: float) -> float:
    """Return sine of x (in radians)"""
    return math.sin(x)

@mcp.tool()
def cos(x: float) -> float:
    """Return cosine of x (in radians)"""
    return math.cos(x)

@mcp.tool()
def tan(x: float) -> float:
    """Return tangent of x (in radians)"""
    return math.tan(x)

@mcp.tool()
def factorial(n: int) -> int:
    """Return factorial of an integer n"""
    if n < 0:
        raise ValueError("Factorial only defined for non-negative integers")
    return math.factorial(n)

@mcp.tool()
def gcd(a: int, b: int) -> int:
    """Return greatest common divisor of two integers"""
    return math.gcd(a, b)

@mcp.tool()
def lcm(a: int, b: int) -> int:
    """Return least common multiple of two integers"""
    return abs(a * b) // math.gcd(a, b)

@mcp.tool()
def mod(a: int, b: int) -> int:
    """Return a modulo b"""
    return a % b

@mcp.tool()
def floor(x: float) -> int:
    """Return the largest integer less than or equal to x"""
    return math.floor(x)

@mcp.tool()
def ceil(x: float) -> int:
    """Return the smallest integer greater than or equal to x"""
    return math.ceil(x)

@mcp.tool()
def round_num(x: float, ndigits: int = 0) -> float:
    """Round a number to the given number of digits (default 0)"""
    return round(x, ndigits)

@mcp.tool()
def matrix_add(a: List[List[float]], b: List[List[float]]) -> List[List[float]]:
    """Matrix addition"""
    return (np.array(a) + np.array(b)).tolist()

@mcp.tool()
def matrix_multiply(a: List[List[float]], b: List[List[float]]) -> List[List[float]]:
    """Matrix multiplication"""
    return (np.matmul(a, b)).tolist()

@mcp.tool()
def matrix_transpose(a: List[List[float]]) -> List[List[float]]:
    """Matrix transpose"""
    return np.transpose(a).tolist()

@mcp.tool()
def matrix_inverse(a: List[List[float]]) -> List[List[float]]:
    """Matrix inverse (square matrix only)"""
    return np.linalg.inv(a).tolist()

@mcp.tool()
def matrix_determinant(a: List[List[float]]) -> float:
    """Matrix determinant"""
    return float(np.linalg.det(a))

# 微积分运算
@mcp.tool()
def derivative(expr: str, var: str = "x") -> str:
    """Take the derivative of an expression with respect to a variable"""
    x = sp.Symbol(var)
    f = sp.sympify(expr)
    return str(sp.diff(f, x))

@mcp.tool()
def integral(expr: str, var: str = "x") -> str:
    """Compute the indefinite integral of an expression with respect to a variable"""
    x = sp.Symbol(var)
    f = sp.sympify(expr)
    return str(sp.integrate(f, x))

@mcp.tool()
def definite_integral(expr: str, var: str = "x", lower: float = 0, upper: float = 1) -> float:
    """Compute the definite integral of an expression from lower to upper bounds"""
    x = sp.Symbol(var)
    f = sp.sympify(expr)
    return float(sp.integrate(f, (x, lower, upper)))

# 求解代数方程
@mcp.tool()
def solve_equation(equation: str, var: str = "x") -> List[str]:
    """Solve an algebraic equation, e.g., 'x**2 - 2 = 0'"""
    x = sp.Symbol(var)
    eq = sp.sympify(equation)
    solutions = sp.solve(eq, x)
    return [str(sol) for sol in solutions]



if __name__ == "__main__":
    mcp.run(transport="stdio")