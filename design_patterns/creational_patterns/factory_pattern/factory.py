"""
factory interface
"""

from abc import ABC, abstractmethod

from product import Button, HTMLButton, WindowsButton

class GUIFactory(ABC):

    def __init__(self) -> None:
        self.button = self.create_button()

    @abstractmethod
    def create_button(self) -> Button:
        raise NotImplementedError("create_button() not implemented")

    def render_button(self):
        return self.button.render()
    
    def on_click_button(self):
        return self.button.onClick()


class HTMLFactory(GUIFactory):
    def create_button(self) -> Button:
        return HTMLButton()


class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()