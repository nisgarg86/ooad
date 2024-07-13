"""
singleton pattern example
"""

from threading import Lock


# class SingletonMeta(type):

#     _instance = None
#     _lock = Lock()

#     def __new__(cls, name, bases, attrs):
#         with cls._lock:
#             if cls._instance is None:
#                 cls._instance = super().__new__(cls, name, bases, attrs)
#         return cls._instance


class Product:

    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, **kwargs):
        if self.__class__._initialized is False:
            self.name = kwargs.get('name', 'product')
            self.price = kwargs.get('price', 0.0)
            self.__class__._initialized = True

    def perform_operation(self, **kwargs):
        print(f'performing operation with kwargs: {kwargs}')
        self.price += kwargs.get('price')
        self.name = kwargs.get('name')
    
    def get_price(self):
        return self.price

    def get_name(self):
        return self.name


if __name__ == '__main__':

    product1 = Product()
    print(id(product1), hash(product1))
    print(f'---- {product1.get_name()} ----- {product1.get_price()} --------')


    product2 = Product()
    print(id(product2), hash(product2))
    print(f'---- {product2.get_name()} ----- {product2.get_price()} --------')
    product2.perform_operation(price=5, name='product2')
    print(f'---- {product2.get_name()} ----- {product2.get_price()} --------')
    
    product3 = Product()
    print(id(product3), hash(product3))
    print(f'---- {product3.get_name()} ----- {product3.get_price()} --------')
    product3.perform_operation(price=10, name='product3')
    print(f'---- {product3.get_name()} ----- {product3.get_price()} --------')