"""
product interface
"""

from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def onClick(self):
        pass

class HTMLButton(Button):
    def render(self):
        return "<button>Click HTML Button!</button>"

    def onClick(self):
        return "HTML Button clicked!"

class WindowsButton(Button):
    def render(self):
        return "<WindowsButton>Click Windows Button!</WindowsButton>"

    def onClick(self):
        return "WindowsButton clicked!"
