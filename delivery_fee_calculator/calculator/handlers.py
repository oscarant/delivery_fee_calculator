from math import ceil
from datetime import datetime
from .schemas import Order, TIME_FORMAT


class DeliveryFeeCalculatorHandler:

    def _small_order_fee(self, order: Order, delivery_fee: int) -> int:
        """
        If the cart value is less than 10€, a small order surcharge is added to the delivery price. The surcharge is
        the difference between the cart value and 10€. For example if the cart value is 8.90€, the surcharge will
        be 1.10€.
        :param order: Received order
        :param delivery_fee: The current delivery fee
        :return: The delivery fee with the small order surcharge added
        """
        if order.cart_value < 1000:
            return delivery_fee + (1000 - order.cart_value)
        else:
            return delivery_fee

    def _distance_fee(self, order: Order, delivery_fee: int) -> int:
        """
        If the delivery distance is more than 1km, a delivery distance surcharge is added to the delivery price.
        :param order: Received order
        :param delivery_fee: The current delivery fee
        :return: The delivery fee with the delivery distance surcharge added
        """
        delivery_fee = delivery_fee + 2000
        if order.delivery_distance > 1000:
            return delivery_fee + ceil((order.delivery_distance - 1000) / 500) * 1000
        else:
            return delivery_fee

    def _number_of_items_fee(self, order: Order, delivery_fee: int) -> int:
        """
        If the number of items is more than 4, a surcharge is added to the delivery price. The surcharge is 50€ per
        item after the 4th item. If the number of items is more than 12, an additional 1.2€ is added to the delivery
        price.
        :param order: Received order
        :param delivery_fee: The current delivery fee
        :return: The delivery fee with the number of items surcharge added
        """
        if order.number_of_items > 4:
            delivery_fee = delivery_fee + (order.number_of_items - 4) * 50
            if order.number_of_items > 12:
                delivery_fee = delivery_fee + 1200
        return delivery_fee

    def _max_fee(self, delivery_fee: int) -> int:
        """
        If the delivery price is more than 15€, the delivery price is capped at 15€.
        :param delivery_fee: The current delivery fee
        :return: The delivery fee capped at 15€
        """
        if delivery_fee > 15000:
            return 15000
        else:
            return delivery_fee

    def _free_delivery(self, order: Order) -> bool:
        """
        If the cart value is more than 100€, the delivery is free.
        :param order: Received order
        :return: True if the delivery is free, False otherwise
        """
        if order.cart_value > 100000:
            return True
        else:
            return False

    def _friday_rush_fee(self, order: Order, delivery_fee: int) -> int:
        """
        If the order is placed on a Friday between 15:00 and 19:00, a 20% surcharge is added to the delivery price.
        :param order: Received order
        :param delivery_fee: The current delivery fee
        :return: The delivery fee with the Friday rush surcharge added
        """
        # Convert the time string to a datetime object
        time = datetime.strptime(order.time, TIME_FORMAT)
        # Check if it's Friday and between 15:00 and 19:00
        if time.weekday() == 4 and 15 <= time.hour <= 19:
            return round(delivery_fee * 1.2)
        else:
            return delivery_fee

    def handle(self, order: Order) -> int:
        """
        Calculate the delivery fee for the given order
        :param order: Received order
        :return: The calculated delivery fee
        """
        delivery_fee = 0
        if self._free_delivery(order=order):
            return delivery_fee
        delivery_fee = self._small_order_fee(order=order, delivery_fee=delivery_fee)
        delivery_fee = self._distance_fee(order=order, delivery_fee=delivery_fee)
        delivery_fee = self._number_of_items_fee(order=order, delivery_fee=delivery_fee)
        delivery_fee = self._friday_rush_fee(order=order, delivery_fee=delivery_fee)
        delivery_fee = self._max_fee(delivery_fee=delivery_fee)
        return delivery_fee
