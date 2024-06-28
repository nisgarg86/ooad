"""
base handler class for chain of responsibility pattern
"""

from abc import ABC, abstractmethod
from typing import Dict

class Handler(ABC):

    def __init__(self) -> None:
        self.__next_handler = None
    
    @abstractmethod
    def handle_request(self, request: Dict[str, str]) -> None:
        if self.__next_handler:
            self.__next_handler.handle_request(request)
        else:
            print('No next handler')

    def set_next_handler(self, handler: Handler):
        self.set_next_handler = handler
