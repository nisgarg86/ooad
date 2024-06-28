"""
utils functions
"""

from typing import Dict

def is_request_authenticated(request: Dict[str, str]) -> bool:
    return request['user'] == 'bob' and request['password'] == '1234'


def is_request_authorized(request: Dict[str, str]) -> bool:
    return request['action'] == 'place_order' and request['user'] == 'bob'


def place_order(request: Dict[str, str]) -> None:
    print('Order placed')