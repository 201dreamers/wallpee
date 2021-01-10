import random
import sys
from typing import Literal

from screeninfo import get_monitors
from screeninfo.common import Monitor, ScreenInfoError

from config import UnsplashConfig


def exit_with_message(msg, exit_code: int = 0) -> None:
    print(f'-- {msg}')
    sys.exit(exit_code)


try:
    monitor: Monitor = get_monitors()[0]
except ScreenInfoError:
    exit_with_message('ERROR: Can\'t get information about your monitor  :(')

Orientation = Literal['landscape', 'portrait', 'square', 'any orientation']


def determine_screen_orientation() -> Orientation:
    """Retrun orientation in string representation.

    Returns same names as in dropdown list on page"""
    if monitor.width > monitor.height:
        return 'landscape'
    elif monitor.width < monitor.height:
        return 'portrait'
    elif monitor.width == monitor.height:
        return 'square'
    return 'any orientation'


def choose_keyword() -> str:
    return random.choice(UnsplashConfig.KEYWORDS)
