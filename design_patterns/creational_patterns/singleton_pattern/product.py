"""
singleton pattern example
"""


class Product:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def perform_operation(self, *args, **kwargs):
        print(f'performing operation with args: {args} and kwargs: {kwargs}')


if __name__ == '__main__':

    product1 = Product()
    print(id(product1), hash(product1))

    product2 = Product()
    print(id(product2), hash(product2))