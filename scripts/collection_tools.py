from general_utils import mini_if
from typing import Union, Callable, Any
from math_functions import *

def get_key(obj: Union[dict, list], *keys: Any, default: Any = None, type: type = None) -> Any:
    """
    Retrieve a nested value from a dictionary or list using a sequence of keys or slices.

    Parameters:
        - obj (Union[dict, list]): The object to retrieve the value from.
        - keys (Any): Sequence of keys or slices to traverse.
        - default (Any): Value to return if retrieval fails or type check fails.
        - type (type): Optional type to check the retrieved value against.

    Returns:
        - result (Any): The retrieved value or the default.

    Examples:
        - get_key({'a': {'b': 2}}, 'a', 'b')  # returns 2
        - get_key({'a': {'b': 2}}, 'a', 'c', default=0)  # returns 0
        - get_key([1, 2, 3], slice(0, 2))  # returns [1, 2]
    """
    try:
        for key in keys:
            obj = obj[key]

        if type is not None and not isinstance(obj, type):
            return default

        return obj

    except (KeyError, TypeError, AttributeError):
        return default

def get_start(obj: Union[dict, list], *keys: Any, default: Any = None, type: type = None) -> Any:
    """
    Retrieve a nested slice from the start to specified indices.

    Parameters:
        - obj (Union[dict, list]): The object to retrieve from.
        - keys (Any): Sequence of slice endpoints.
        - default (Any): Value to return if retrieval fails.
        - type (type): Optional type to enforce on the retrieved value.

    Returns:
        - result (Any): The sliced value or default.

    Examples:
        - get_start([1,2,3,4], 2)  # returns [1, 2]
        - get_start({'a': [1,2,3]}, 'a', 2)  # returns [1, 2]
    """
    return get_key(obj, *(slice(None, key) for key in keys), default=default, type=type)

def get_end(obj: Union[dict, list], *keys: Any, default: Any = None, type: type = None) -> Any:
    """
    Retrieve a nested slice from specified indices to the end.

    Parameters:
        - obj (Union[dict, list]): The object to retrieve from.
        - keys (Any): Sequence of slice start points.
        - default (Any): Value to return if retrieval fails.
        - type (type): Optional type to enforce on the retrieved value.

    Returns:
        - result (Any): The sliced value or default.

    Examples:
        - get_end([1,2,3,4], 2)  # returns [3, 4]
        - get_end({'a': [1,2,3]}, 'a', 1)  # returns [2, 3]
    """
    return get_key(obj, *(slice(key, None) for key in keys), default=default, type=type)

def set_key(obj: Union[dict, list], *keys: Any) -> Callable[[Any], None]:
    """
    Generate a setter function to assign a value at a nested location.

    Parameters:
        - obj (Union[dict, list]): The object to modify.
        - keys (Any): Sequence of keys to locate the nested position.

    Returns:
        - setter (Callable[[Any], None]): A function that sets the value.

    Examples:
        - setter = set_key({'a': {'b': 0}}, 'a', 'b'); setter(5)  # sets obj['a']['b'] = 5
    """
    def setter(value: Any):
        current = obj

        for key in get_start(keys, -1):
            current = get_key(current, key)

        current[keys[-1]] = value

    return setter

def delete_key(obj: Union[dict, list], *keys: Any) -> bool:
    """
    Delete a key from a nested dictionary or list safely.

    Parameters:
        - obj (Union[dict, list]): The object to modify.
        - keys (Any): Sequence of keys to locate the nested position.

    Returns:
        - success (bool): True if deletion succeeded, False otherwise.

    Examples:
        - delete_key({'a': {'b': 2}}, 'a', 'b')  # returns True
        - delete_key({'a': {'b': 2}}, 'a', 'c')  # returns False
    """
    try:
        for key in get_start(keys, -1):
            obj = get_key(obj, key)

        del obj[keys[-1]]
        return True

    except (KeyError, TypeError, AttributeError):
        return False

def key_exists(obj: Union[dict, list], key: Any) -> bool:
    """
    Check if a key exists in a dictionary or list.

    Parameters:
        - obj (Union[dict, list]): The object to check.
        - key (Any): Key to check for existence.

    Returns:
        - exists (bool): True if key exists, False otherwise.

    Examples:
        - key_exists({'a': 1}, 'a')  # True
        - key_exists([1,2], 3)  # False
    """
    return key in obj

def merge_json(json1: dict, json2: dict) -> dict:
    """
    Recursively merge two dictionaries.

    Parameters:
        - json1 (dict): Base dictionary to update.
        - json2 (dict): Dictionary to merge into json1.

    Returns:
        - result (dict): Merged dictionary.

    Examples:
        - merge_json({'a':1}, {'b':2})  # {'a':1, 'b':2}
        - merge_json({'a': {'x':1}}, {'a': {'y':2}})  # {'a': {'x':1, 'y':2}}
    """
    for key, value in json2.items():
        if isinstance(value, dict) and isinstance(get_key(json1, key), dict) and key_exists(json1, key):
            merge_json(get_key(json1, key), value)
        else:
            set_key(json1, key)(value)

    return json1

def dictify_list(obj: list, value: Any = 0, value_func: Callable = None) -> dict:
    """
    Convert a list into a dictionary with uniform values or computed values.

    Parameters:
        - obj (list): List of keys to convert.
        - value (Any): Value to assign for all keys if value_func is None.
        - value_func (Callable): Optional function to compute value for each key.

    Returns:
        - result (dict): Dictionary with keys from the list and assigned values.

    Examples:
        - dictify_list(['a','b'], 1)  # {'a':1, 'b':1}
        - dictify_list(['a','b'], value_func=lambda x: ord(x))  # {'a':97, 'b':98}
    """
    if not isinstance(obj, list):
        return obj

    if value_func is not None:
        return {key: value_func(key) for key in obj}

    return {key: value for key in obj}

def map_list(data: Union[list, tuple], operation: str, value: Any = None) -> Union[list, tuple]:
    """
    Apply a mathematical operation to each element in a list or tuple.

    Parameters:
        - data (Union[list, tuple]): Iterable of numbers to operate on.
        - operation (str): Operation name (e.g., 'add', 'multiply', 'sin').
        - value (Any): Optional second operand for operations.

    Returns:
        - result (Union[list, tuple]): Transformed list or tuple after applying the operation.

    Examples:
        - map_list([1,2,3], 'add', 2)  # [3,4,5]
        - map_list((1,4,9), 'sqrt')  # [1.0, 2.0, 3.0]
        - map_list([1,2,3], 'negate')  # [-1,-2,-3]
    """
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide,
        'pow': pow,
        'base_pow': base_pow,
        'inv_pow': inv_pow,
        'root': root,
        'negate': negate,
        'mod': mod,
        'floor': floor,
        'round': round_func,
        'ceil': ceil,
        'truncate': truncate,
        'floordiv': floordiv,
        'rounddiv': rounddiv,
        'ceildiv': ceildiv,
        'truncatediv': truncatediv,
        'log': log,
        'ln': ln,
        'abs': absify,
        'factorial': fact,
        'sin': sin,
        'cos': cos,
        'tan': tan,
        'arcsin': arcsin,
        'arccos': arccos,
        'arctan': arctan,
        'arctan2': arctan2,
        'sinh': sinh,
        'cosh': cosh,
        'tanh': tanh,
        'arcsinh': arcsinh,
        'arccosh': arccosh,
        'arctanh': arctanh,
        'sign': sign,
        'exp': exp,
        'cosec': cosec,
        'sec': sec,
        'cot': cot,
        'cosech': cosech,
        'sech': sech,
        'coth': coth,
        'tostring': tostring,
        'tostring_fmt': tostring_fmt
    }

    func = get_key(operations, operation)

    if func is None:
        raise ValueError(f"Operation '{operation}' is not supported")

    result = [mini_if(value is None, func(x), func(x, value)) for x in data]

    if isinstance(data, tuple):
        return tuple(result)

    return result