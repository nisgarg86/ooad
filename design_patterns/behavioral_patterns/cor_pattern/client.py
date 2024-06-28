"""
client code for the chain of responsibility pattern
"""

from typing import Dict

from handlers import AuthorizationHandler, AuthenticationHandler, PlaceOrderHandler

def main(request: Dict[str, str]):

    authorization_handler = AuthorizationHandler()
    authentication_handler = AuthenticationHandler()
    place_order_handler = PlaceOrderHandler()

    authorization_handler.set_next_handler(authentication_handler)
    authentication_handler.set_next_handler(place_order_handler)

    authorization_handler.handle_request(request)


if __name__ == '__main__':
    request = {'user': 'bob',
               'password': '1234',
               'action': 'place_order',
               'order': '1'}
    main(request)

    request = {'user': 'alice',
                'password': '5678',
                'action': 'place_order',
                'order': '2'}
    main(request)

    request = {'user': 'bob',
                'password': '1234',
                'action': 'cancel_order',
                'order': '3'}
    main(request)