from clients.basis.abstract_client import AbstractClient


class UnsplashClient(AbstractClient):

    __slots__ = ()

    def __init__(self, driver):
        self.driver = driver
