from math import ceil
import datetime


def small_order_fee(order, delivery_fee) -> int:
    if order.cart_value < 1000:
        return delivery_fee + (1000 - order.cart_value)
    else:
        return delivery_fee


def distance_fee(order, delivery_fee) -> int:
    delivery_fee + 2000
    if order.distance > 1000:
        return delivery_fee + ceil((order.distance - 1000) / 500) * 1000
    else:
        return delivery_fee


def number_of_items_fee(order, delivery_fee) -> int:
    if order.number_of_items > 4:
        delivery_fee = delivery_fee + (order.number_of_items - 4) * 50
        if order.number_of_items > 12:
            delivery_fee = delivery_fee + 1200
    return delivery_fee


def max_fee(delivery_fee) -> int:
    if delivery_fee > 15000:
        return 15000
    else:
        return delivery_fee


def free_delivery(order, delivery_fee) -> int:
    if order.cart_value > 100000:
        return 0
    else:
        return delivery_fee


def friday_rush_fee(order, delivery_fee) -> int:
    time = datetime.datetime.fromisoformat(order.time)
    # Check if it's Friday and between 15:00 and 19:00
    if time.weekday() == 4 and 15 <= time.hour <= 19:
        return round(delivery_fee * 1.2)
    else:
        return delivery_fee


def calculate_delivery_fee(order) -> int:
    delivery_fee = 0
    if free_delivery(order, delivery_fee) == 0:
        return delivery_fee
    delivery_fee = small_order_fee(order, delivery_fee)
    delivery_fee = distance_fee(order, delivery_fee)
    delivery_fee = number_of_items_fee(order, delivery_fee)
    delivery_fee = friday_rush_fee(order, delivery_fee)
    delivery_fee = max_fee(delivery_fee)
    return delivery_fee
