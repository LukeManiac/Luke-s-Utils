import math
from typing import Union, Optional, Any

Number = Union[int, float]

def add(x: Number, y: Number = 0) -> Number:
    """
    Add two numbers.

    Parameters:
        - x (Number): First number.
        - y (Number): Second number (default 0).

    Returns:
        - result (Number): Sum of x and y.

    Examples:
        - add(2, 3)  # 5
        - add(5)  # 5
    """
    return x + y


def subtract(x: Number, y: Number = 0) -> Number:
    """
    Subtract y from x.

    Parameters:
        - x (Number): Minuend.
        - y (Number): Subtrahend (default 0).

    Returns:
        - result (Number): Difference of x and y.

    Examples:
        - subtract(5, 2)  # 3
        - subtract(5)  # 5
    """
    return add(x, -y)


def multiply(x: Number, y: Number = 1) -> Number:
    """
    Multiply two numbers.

    Parameters:
        - x (Number): First number.
        - y (Number): Second number (default 1).

    Returns:
        - result (Number): Product of x and y.

    Examples:
        - multiply(2, 3)  # 6
        - multiply(5)  # 5
    """
    return x * y


def divide(x: Number, y: Number = 1) -> float:
    """
    Divide x by y.

    Parameters:
        - x (Number): Numerator.
        - y (Number): Denominator (default 1).

    Returns:
        - result (float): Result of division.

    Examples:
        - divide(6, 3)  # 2.0
        - divide(5)  # 5.0
    """
    return multiply(x, 1 / y)


def base_pow(x: Number, y: Number = 1) -> float:
    """
    Raise y to the power of x.

    Parameters:
        - x (Number): Exponent.
        - y (Number): Base (default 1).

    Returns:
        - result (float): y raised to the power x.

    Examples:
        - base_pow(2, 3)  # 9
        - base_pow(3)  # 1
    """
    return pow(y, x)


def inv_pow(x: Number, y: Number = 1) -> float:
    """
    Compute x raised to the power of -y.

    Parameters:
        - x (Number): Base.
        - y (Number): Exponent (default 1).

    Returns:
        - result (float): x ** (-y).

    Examples:
        - inv_pow(2, 3)  # 0.125
        - inv_pow(4)  # 1/4
    """
    return pow(x, -y)


def root(x: Number, y: Number = 1) -> float:
    """
    Compute the y-th root of x.

    Parameters:
        - x (Number): Value to root.
        - y (Number): Root degree (default 1).

    Returns:
        - result (float): x ** (1/y).

    Examples:
        - root(9, 2)  # 3.0
        - root(8, 3)  # 2.0
    """
    return pow(x, 1 / y)


def negate(x: Number, y: Number = 1) -> Number:
    """
    Multiply x by -y to negate or scale negatively.

    Parameters:
        - x (Number): Value to negate.
        - y (Number): Scaling factor (default 1).

    Returns:
        - result (Number): Negative scaled value.

    Examples:
        - negate(5)  # -5
        - negate(5, 2)  # -10
    """
    return multiply(x, -y)


def mod(x: Number, y: Number = 1) -> Number:
    """
    Compute x modulo y.

    Parameters:
        - x (Number): Dividend.
        - y (Number): Divisor (default 1).

    Returns:
        - result (Number): Remainder of x / y.

    Examples:
        - mod(5, 2)  # 1
        - mod(7)  # 0
    """
    return x % y


def floor(x: Number, y: Number = 1) -> int:
    """
    Multiply x by y and return the floor.

    Parameters:
        - x (Number): Value.
        - y (Number): Scaling factor (default 1).

    Returns:
        - result (int): Floor of scaled value.

    Examples:
        - floor(2.7)  # 2
        - floor(2.7, 2)  # 5
    """
    return math.floor(multiply(x, y))


def round_func(x: Number, y: Number = 1) -> int:
    """
    Multiply x by y and round to nearest integer.

    Parameters:
        - x (Number): Value.
        - y (Number): Scaling factor (default 1).

    Returns:
        - result (int): Rounded value.

    Examples:
        - round_func(2.3)  # 2
        - round_func(2.7)  # 3
    """
    return round(multiply(x, y))


def ceil(x: Number, y: Number = 1) -> int:
    """
    Multiply x by y and return the ceiling.

    Parameters:
        - x (Number): Value.
        - y (Number): Scaling factor (default 1).

    Returns:
        - result (int): Ceiling of scaled value.

    Examples:
        - ceil(2.3)  # 3
        - ceil(2.7)  # 3
    """
    return math.ceil(multiply(x, y))


def truncate(x: Number, y: Number = 1) -> int:
    """
    Multiply x by y and truncate to integer.

    Parameters:
        - x (Number): Value.
        - y (Number): Scaling factor (default 1).

    Returns:
        - result (int): Truncated value.

    Examples:
        - truncate(2.9)  # 2
        - truncate(2.1, 2)  # 4
    """
    return math.trunc(multiply(x, y))


def floordiv(x: Number, y: Number = 1) -> int:
    """
    Divide x by y and return floor.

    Parameters:
        - x (Number): Dividend.
        - y (Number): Divisor (default 1).

    Returns:
        - result (int): Floor of division.

    Examples:
        - floordiv(7, 2)  # 3
        - floordiv(5)  # 5
    """
    return floor(x, 1 / y)


def rounddiv(x: Number, y: Number = 1) -> int:
    """
    Divide x by y and round to nearest integer.

    Parameters:
        - x (Number): Dividend.
        - y (Number): Divisor (default 1).

    Returns:
        - result (int): Rounded division result.

    Examples:
        - rounddiv(7, 2)  # 4
        - rounddiv(5)  # 5
    """
    return round_func(x, 1 / y)


def ceildiv(x: Number, y: Number = 1) -> int:
    """
    Divide x by y and return ceiling.

    Parameters:
        - x (Number): Dividend.
        - y (Number): Divisor (default 1).

    Returns:
        - result (int): Ceiling of division.

    Examples:
        - ceildiv(7, 2)  # 4
        - ceildiv(5)  # 5
    """
    return ceil(x, 1 / y)


def truncatediv(x: Number, y: Number = 1) -> int:
    """
    Divide x by y and truncate.

    Parameters:
        - x (Number): Dividend.
        - y (Number): Divisor (default 1).

    Returns:
        - result (int): Truncated division.

    Examples:
        - truncatediv(7, 2)  # 3
        - truncatediv(5)  # 5
    """
    return truncate(x, 1 / y)


def log(x: Number, y: Number = 10) -> float:
    """
    Compute logarithm of x with base y.

    Parameters:
        - x (Number): Value.
        - y (Number): Base (default 10).

    Returns:
        - result (float): log_y(x)

    Examples:
        - log(100)  # 2.0
        - log(8, 2)  # 3.0
    """
    return math.log(x, y)


def ln(x: Number, y: Optional[Number] = None) -> float:
    """
    Compute natural logarithm of x.

    Parameters:
        - x (Number): Value.
        - y: Ignored parameter for compatibility.

    Returns:
        - result (float): ln(x)

    Examples:
        - ln(math.e)  # 1.0
    """
    return math.log(x, math.e)


def absify(x: Number, y: Optional[Number] = None) -> Number:
    """
    Return absolute value of x.

    Parameters:
        - x (Number): Value.
        - y: Ignored for compatibility.

    Returns:
        - result (Number): Absolute value.

    Examples:
        - absify(-5)  # 5
    """
    return abs(x)


def fact(x: Number, y: Optional[Number] = None) -> int:
    """
    Compute factorial of x.

    Parameters:
        - x (Number): Value to factorial.
        - y: Ignored for compatibility.

    Returns:
        - result (int): Factorial of int(x).

    Examples:
        - fact(5)  # 120
    """
    return math.factorial(int(x))

def sin(x: Number, y: Number = 1) -> float:
    """
    Compute sine of x multiplied by y.

    Parameters:
        - x (Number): Angle in radians.
        - y (Number): Scaling factor (default 1).

    Returns:
        - result (float): sin(x * y)

    Examples:
        - sin(math.pi / 2)  # 1.0
        - sin(math.pi / 4, 2)  # sin(pi/2) -> 1.0
    """
    return math.sin(multiply(x, y))


def cos(x: Number, y: Number = 1) -> float:
    """
    Compute cosine of x multiplied by y.

    Parameters:
        - x (Number): Angle in radians.
        - y (Number): Scaling factor (default 1).

    Returns:
        - result (float): cos(x * y)
    """
    return math.cos(multiply(x, y))


def tan(x: Number, y: Number = 1) -> float:
    """
    Compute tangent of x multiplied by y.

    Parameters:
        - x (Number): Angle in radians.
        - y (Number): Scaling factor (default 1).

    Returns:
        - result (float): tan(x * y)
    """
    return math.tan(multiply(x, y))


def arcsin(x: Number, y: Number = 1) -> float:
    """
    Compute arcsine of x multiplied by y.

    Parameters:
        - x (Number): Input value.
        - y (Number): Scaling factor (default 1).

    Returns:
        - result (float): arcsin(x * y)
    """
    return math.asin(multiply(x, y))


def arccos(x: Number, y: Number = 1) -> float:
    """
    Compute arccosine of x multiplied by y.

    Parameters:
        - x (Number): Input value.
        - y (Number): Scaling factor (default 1).

    Returns:
        - result (float): arccos(x * y)
    """
    return math.acos(multiply(x, y))


def arctan(x: Number, y: Number = 1) -> float:
    """
    Compute arctangent of x multiplied by y.

    Parameters:
        - x (Number): Input value.
        - y (Number): Scaling factor (default 1).

    Returns:
        - result (float): arctan(x * y)
    """
    return math.atan(multiply(x, y))


def arctan2(x: Number, y: Number = 1) -> float:
    """
    Compute arctangent of y/x using two arguments.

    Parameters:
        - x (Number): x-coordinate.
        - y (Number): y-coordinate (default 1).

    Returns:
        - result (float): arctan2(y, x)

    Examples:
        - arctan2(1, 1)  # pi/4
    """
    return math.atan2(y, x)


def sinh(x: Number, y: Number = 1) -> float:
    """
    Compute hyperbolic sine of x multiplied by y.

    Parameters:
        - x (Number): Input value.
        - y (Number): Scaling factor (default 1).

    Returns:
        - result (float): sinh(x * y)
    """
    return math.sinh(multiply(x, y))


def cosh(x: Number, y: Number = 1) -> float:
    """
    Compute hyperbolic cosine of x multiplied by y.

    Parameters:
        - x (Number): Input value.
        - y (Number): Scaling factor (default 1).

    Returns:
        - result (float): cosh(x * y)
    """
    return math.cosh(multiply(x, y))


def tanh(x: Number, y: Number = 1) -> float:
    """
    Compute hyperbolic tangent of x multiplied by y.

    Parameters:
        - x (Number): Input value.
        - y (Number): Scaling factor (default 1).

    Returns:
        - result (float): tanh(x * y)
    """
    return math.tanh(multiply(x, y))


def sign(x: Number, y: Number = 1) -> int:
    """
    Return the sign of x multiplied by y.

    Parameters:
        - x (Number): Input value.
        - y (Number): Scaling factor (default 1).

    Returns:
        - result (int): -y if x < 0, y if x > 0, 0 if x == 0

    Examples:
        - sign(5)  # 1
        - sign(-3, 2)  # -2
    """
    if x == 0:
        return x
    return int(math.copysign(y, x))


def exp(x: Number, y: Number = 1) -> float:
    """
    Compute e^(x*y).

    Parameters:
        - x (Number): Exponent.
        - y (Number): Scaling factor (default 1).

    Returns:
        - result (float): e^(x*y)
    """
    return math.exp(multiply(x, y))


def cosec(x: Number, y: Number = 1) -> float:
    """
    Compute cosecant (1/sin) of x*y.

    Parameters:
        - x (Number): Angle in radians.
        - y (Number): Scaling factor (default 1).

    Returns:
        - result (float): 1 / sin(x*y)
    """
    return inv_pow(sin(x, y))


def sec(x: Number, y: Number = 1) -> float:
    """
    Compute secant (1/cos) of x*y.

    Parameters:
        - x (Number): Angle in radians.
        - y (Number): Scaling factor (default 1).

    Returns:
        - result (float): 1 / cos(x*y)
    """
    return inv_pow(cos(x, y))


def cot(x: Number, y: Number = 1) -> float:
    """
    Compute cotangent (1/tan) of x*y.

    Parameters:
        - x (Number): Angle in radians.
        - y (Number): Scaling factor (default 1).

    Returns:
        - result (float): 1 / tan(x*y)
    """
    return inv_pow(tan(x, y))


def cosech(x: Number, y: Number = 1) -> float:
    """
    Compute hyperbolic cosecant (1/sinh) of x*y.

    Parameters:
        - x (Number): Input value.
        - y (Number): Scaling factor (default 1).

    Returns:
        - result (float): 1 / sinh(x*y)
    """
    return inv_pow(sinh(x, y))


def sech(x: Number, y: Number = 1) -> float:
    """
    Compute hyperbolic secant (1/cosh) of x*y.

    Parameters:
        - x (Number): Input value.
        - y (Number): Scaling factor (default 1).

    Returns:
        - result (float): 1 / cosh(x*y)
    """
    return inv_pow(cosh(x, y))


def coth(x: Number, y: Number = 1) -> float:
    """
    Compute hyperbolic cotangent (1/tanh) of x*y.

    Parameters:
        - x (Number): Input value.
        - y (Number): Scaling factor (default 1).

    Returns:
        - result (float): 1 / tanh(x*y)
    """
    return inv_pow(tanh(x, y))


def arcsinh(x: Number, y: Number = 1) -> float:
    """
    Compute inverse hyperbolic sine of x*y.

    Parameters:
        - x (Number): Input value.
        - y (Number): Scaling factor (default 1).

    Returns:
        - result (float): arcsinh(x*y)
    """
    return arcsin(x, y)


def arccosh(x: Number, y: Number = 1) -> float:
    """
    Compute inverse hyperbolic cosine of x*y.

    Parameters:
        - x (Number): Input value.
        - y (Number): Scaling factor (default 1).

    Returns:
        - result (float): arccosh(x*y)
    """
    return arccos(x, y)


def arctanh(x: Number, y: Number = 1) -> float:
    """
    Compute inverse hyperbolic tangent of x*y.

    Parameters:
        - x (Number): Input value.
        - y (Number): Scaling factor (default 1).

    Returns:
        - result (float): arctanh(x*y)
    """
    return arctan(x, y)


def tostring(x: Any, y: Optional[Number] = None) -> str:
    """
    Convert a value to string.

    Parameters:
        - x (Any): Value to convert.
        - y: Ignored for compatibility.

    Returns:
        - result (str): String representation of x
    """
    return str(x)


def tostring_fmt(x: Number, y: int = 0) -> str:
    """
    Convert a number to a formatted string with y decimal places.

    Parameters:
        - x (Number): Value to format.
        - y (int): Number of decimal places.

    Returns:
        - result (str): Formatted string representation.

    Examples:
        - tostring_fmt(3.14159, 2)  # '3.14'
        - tostring_fmt(5)  # '5.00'
    """
    try:
        return format(x, f".{y}f")
    except (ValueError, TypeError):
        return tostring(x)