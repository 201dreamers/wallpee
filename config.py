import os


class WallpeeConfig:

    __slots__ = ()

    NAME = 'Wallpee'
    VERSION = '0.0.1'
    DEFAULT_PATH = os.getenv('HOME')
