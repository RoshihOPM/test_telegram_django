from abc import ABC, abstractmethod


class BaseHandler(ABC):
    @abstractmethod
    def handle(self, *args, **kwargs):
        pass
