from abc import ABC, abstractmethod


class AbstractClient(ABC):

    @abstractmethod
    def get_random_image(self):
        pass
