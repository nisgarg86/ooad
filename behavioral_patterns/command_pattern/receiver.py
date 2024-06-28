"""
utils.py: Contains utility functions for the command pattern.
"""

class OrderSystem:

    def order_queue(self, user_id: str, item_code: str, quantity: int) -> None:
        print(f'Request for Order queued for user {user_id} for item {item_code} with quantity {quantity}')

    def cancel_queue(self, order_id: str) -> None:
        print(f'Request for Order cancellation queued for order id {order_id}')
