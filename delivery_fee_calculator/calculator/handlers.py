from math import ceil
from datetime import datetime
from .schemas import Order, TIME_FORMAT


class DeliveryFeeCalculatorHandler:

    def _small_order_fee(self, order: Order, delivery_fee: int) -> int:
        if order.cart_value < 1000:
            return delivery_fee + (1000 - order.cart_value)
        else:
            return delivery_fee

    def _distance_fee(self, order: Order, delivery_fee: int) -> int:
        delivery_fee = delivery_fee + 2000
        if order.delivery_distance > 1000:
            return delivery_fee + ceil((order.delivery_distance - 1000) / 500) * 1000
        else:
            return delivery_fee

    def _number_of_items_fee(self, order: Order, delivery_fee: int) -> int:
        if order.number_of_items > 4:
            delivery_fee = delivery_fee + (order.number_of_items - 4) * 50
            if order.number_of_items > 12:
                delivery_fee = delivery_fee + 1200
        return delivery_fee

    def _max_fee(self, delivery_fee: int) -> int:
        if delivery_fee > 15000:
            return 15000
        else:
            return delivery_fee

    def _free_delivery(self, order: Order) -> bool:
        if order.cart_value > 100000:
            return True
        else:
            return False

    def _friday_rush_fee(self, order: Order, delivery_fee: int) -> int:
        time = datetime.strptime(order.time, TIME_FORMAT)
        # Check if it's Friday and between 15:00 and 19:00
        if time.weekday() == 4 and 15 <= time.hour <= 19:
            return round(delivery_fee * 1.2)
        else:
            return delivery_fee

    def handle(self, order: Order) -> int:
        delivery_fee = 0
        if self._free_delivery(order):
            return delivery_fee
        delivery_fee = self._small_order_fee(order, delivery_fee)
        delivery_fee = self._distance_fee(order, delivery_fee)
        delivery_fee = self._number_of_items_fee(order, delivery_fee)
        delivery_fee = self._friday_rush_fee(order, delivery_fee)
        delivery_fee = self._max_fee(delivery_fee)
        return delivery_fee
