"""
concrete handlers for the chain of responsibility pattern
"""

from typing import Dict
from abstract_handler import Handler
from utils import is_request_authenticated, is_request_authorized, place_order


class AuthorizationHandler(Handler):

    def handle_request(self, request: Dict[str, str]) -> None:
        if is_request_authorized(request):
            print('Request authorized')
            super().handle_request(request)
        else:
            print('Request not authorized, dropping request')


class AuthenticationHandler(Handler):

    def handle_request(self, request: Dict[str, str]) -> None:
        if is_request_authenticated(request):
            print('Request authenticated')
            super().handle_request(request)
        else:
            print('Request not authenticated, dropping request')


class PlaceOrderHandler(Handler):

    def handle_request(self, request: str) -> None:
        place_order(request)