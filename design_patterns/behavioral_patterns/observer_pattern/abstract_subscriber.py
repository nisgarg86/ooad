"""
abstract class for subscriber
"""

from abc import ABC, abstractmethod


class AbstractSubscriber(ABC):

    @abstractmethod
    def update(self, *args, **kwargs):
        pass
