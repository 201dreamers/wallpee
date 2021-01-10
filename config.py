import os


class WallpeeConfig:

    __slots__ = ()

    NAME = 'Wallpee'
    VERSION = '0.0.1'
    DEFAULT_PATH = os.getenv('HOME')


class DefaultConfig:

    __slots__ = ()

    TIMEOUT = 10


class UnsplashConfig(DefaultConfig):

    __slots__ = ()

    URL = 'https://unsplash.com'
    KEYWORDS = ('wallpaper', 'desktop-background', 'desktop-wallpaper')
    IMAGE_WIDTHS = (640, 1920, 2400)
