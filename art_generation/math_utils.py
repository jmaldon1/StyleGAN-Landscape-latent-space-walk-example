from typing import List
import math

from opensimplex import OpenSimplex


def constrain(n: int, low: int, high: int) -> int:
    """
    Constrains a value between a minimum and maximum value.
    """
    return max(min(n, high), low)


def remap(
    n: int, start1: int, stop1: int, start2: int, stop2: int, withinBounds: bool = True
) -> int:
    """
    Re-maps a number from one range to another.
    """
    newval = (n - start1) / (stop1 - start1) * (stop2 - start2) + start2
    if not withinBounds:
        return newval
    if start2 < stop2:
        return constrain(newval, start2, stop2)
    else:
        return constrain(newval, stop2, start2)


def generate_noise(
    cx: int, cy: int, angle: int, diameter: int, tmp: OpenSimplex, minimum: int = -1, maximum: int = 1
) -> int:
    """
    2-dimensional gradient noise function
    """

    xoff = remap(math.cos(angle), -1, 1, cx, cx + diameter)
    yoff = remap(math.sin(angle), -1, 1, cy, cy + diameter)
    r = tmp.noise2d(x=xoff, y=yoff)
    return remap(r, -1, 1, minimum, maximum)


def random_noise_sample(
    size: int,
    cxs: List[int],
    cys: List[int],
    angle: int,
    diameter: int,
    tmp: OpenSimplex,
    minimum: int = -1,
    maximum: int = 1
) -> List[float]:
    """
    Create a random sample of noise
    """
    assert len(cxs) == size
    assert len(cys) == size

    sample = []
    for i in range(size):
        sample.append(generate_noise(cxs[i], cys[i], angle, diameter, tmp, minimum, maximum))
    
    return sample
