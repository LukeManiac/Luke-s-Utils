from typing import Union, Any

def mini_if(condition: bool, true: Any = True, false: Any = False) -> Any:
    """
    Return one of two values depending on a condition.

    Parameters:
        - condition (bool): The condition to evaluate.
        - true (Any): Value to return if condition is True.
        - false (Any): Value to return if condition is False.

    Returns:
        - result (Any): Either `true` or `false` depending on the condition.

    Examples:
        - mini_if(True, 'yes', 'no')  # returns 'yes'
        - mini_if(False, 1, 0)  # returns 0
        - mini_if(5 > 3, [1,2], [3,4])  # returns [1,2]
    """
    return true if condition else false

def lerp(start: Union[int, float], stop: Union[int, float], step: float) -> Union[int, float]:
    """
    Perform linear interpolation between two values.

    Parameters:
        - start (Union[int, float]): Starting value.
        - stop (Union[int, float]): Ending value.
        - step (float): Interpolation factor between 0.0 and 1.0.

    Returns:
        - result (Union[int, float]): Interpolated value.

    Examples:
        - lerp(0, 10, 0.5)  # returns 5
        - lerp(100, 200, 0.25)  # returns 125
        - lerp(-5, 5, 0.7)  # returns 2.0
    """
    return start + (stop - start) * step