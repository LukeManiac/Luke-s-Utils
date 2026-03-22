import colorsys as coloursys
from general_utils import lerp
from typing import Tuple, Union

Colour = Tuple[Union[int, float], Union[int, float], Union[int, float]]

def rainbow(timer: float = 0, hue_speed: float = 1, saturation: float = 1, value: float = 1) -> Colour:
    """
    Generate an RGB colour cycling through the rainbow based on a timer.

    Parameters:
        - timer (float): Time or step used to calculate hue.
        - hue_speed (float): Speed multiplier for hue change.
        - saturation (float): Saturation of the colour (0 to 1).
        - value (float): Value/brightness of the colour (0 to 1).

    Returns:
        - colour (Tuple[float, float, float]): RGB colour values in the range 0-1.

    Examples:
        - rainbow(0)  # returns (1.0, 0.0, 0.0)
        - rainbow(0.5, hue_speed=2)  # returns mid-rainbow colour
    """
    return (channel * 255 for channel in coloursys.hsv_to_rgb((timer * hue_speed) % 1, saturation, value))

def lerp_colour(colour1: Colour, colour2: Colour, step: float, use_hsv: bool = False, find_closest_hue: bool = False, return_int: bool = False) -> Colour:
    """
    Interpolate between two colours, optionally using HSV space and handling hue wrap-around.

    Parameters:
        - colour1 (Tuple[int, float, float]): The starting colour as RGB.
        - colour2 (Tuple[int, float, float]): The ending colour as RGB.
        - step (float): Interpolation factor (0.0 to 1.0).
        - use_hsv (bool): If True, interpolation occurs in HSV space.
        - find_closest_hue (bool): If True, chooses shortest path around the hue circle.
        - return_int (bool): If True, returns RGB values as integers (0-255).

    Returns:
        - output (Tuple[Union[int, float], Union[int, float], Union[int, float]]): Interpolated colour.

    Examples:
        - lerp_colour((255,0,0), (0,0,255), 0.5)  # returns (127, 0, 127)
        - lerp_colour((255,0,0), (0,0,255), 0.5, use_hsv=True)  # HSV interpolation
        - lerp_colour((255,0,0), (0,0,255), 0.5, return_int=True)  # returns integer RGB
    """
    if use_hsv:
        h1, s1, v1 = coloursys.rgb_to_hsv(*(c / 255 for c in colour1))
        h2, s2, v2 = coloursys.rgb_to_hsv(*(c / 255 for c in colour2))

        if find_closest_hue:
            dh = h2 - h1

            if dh > 0.5:
                dh -= 1
            elif dh < -0.5:
                dh += 1

            h = (h1 + dh * step) % 1.0
        else:
            h = lerp(h1, h2, step)

        s = lerp(s1, s2, step)
        v = lerp(v1, v2, step)

        output: Tuple[float, float, float] = coloursys.hsv_to_rgb(h, s, v)
    else:
        output: Tuple[int, int, int] = tuple(int(lerp(start, end, step)) for start, end in zip(colour1, colour2))

    if return_int:
        output = tuple(int(x * 255) if isinstance(x, float) and x <= 1 else int(x) for x in output)

    return output
