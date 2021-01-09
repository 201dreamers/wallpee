import random
from typing import Literal

from screeninfo import get_monitors
from screeninfo.common import Monitor

from config import UnsplashConfig


Orientation = Literal['landscape', 'portrait', 'square', 'any orientation']


def determine_screen_orientation() -> Orientation:
    """Retrun orientation in string representation.

    Returns same names as in dropdown list on page"""
    monitor: Monitor = get_monitors()[0]
    if monitor.width > monitor.height:
        return 'landscape'
    elif monitor.width < monitor.height:
        return 'portrait'
    elif monitor.width == monitor.height:
        return 'square'
    return 'any orientation'


def determine_keyword():
    return random.choice(UnsplashConfig.KEYWORDS)
