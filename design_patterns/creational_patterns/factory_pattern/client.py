"""
Client code to test the factory pattern implementation.
"""

from factory import HTMLFactory, WindowsFactory


class Client:

    def __init__(self, factory_type: str) -> None:
        if factory_type == "HTML":
            self.factory = HTMLFactory()
        elif factory_type == "Windows":
            self.factory = WindowsFactory()
        else:
            raise ValueError("Unknown factory type")

    def render_button(self):
        return self.factory.render_button()

    def on_click_button(self):
        return self.factory.on_click_button()


if __name__ == "__main__":

    client = Client("HTML")
    print(client.render_button())
    print(client.on_click_button())

    client = Client("Windows")
    print(client.render_button())
    print(client.on_click_button())