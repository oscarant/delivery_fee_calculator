import unittest

from delivery_fee_calculator.calculator.handlers import DeliveryFeeCalculatorHandler
from delivery_fee_calculator.calculator.schemas import Order


class TestHandlers(unittest.TestCase):
    def test_small_order_fee(self):
        order = Order(
            cart_value=1000,
            delivery_distance=1000,
            number_of_items=4,
            time="2021-01-16T12:00:00Z"
        )
        expected = 0
        actual = DeliveryFeeCalculatorHandler()._small_order_fee(order=order, delivery_fee=0)
        self.assertEqual(actual, expected)

    def test_small_order_fee_1(self):
        order = Order(
            cart_value=999,
            delivery_distance=1000,
            number_of_items=4,
            time="2021-01-16T12:00:00Z"
        )
        expected = 1
        actual = DeliveryFeeCalculatorHandler()._small_order_fee(order=order, delivery_fee=0)
        self.assertEqual(actual, expected)

    def test_small_order_fee_2(self):
        order = Order(
            cart_value=0,
            delivery_distance=1000,
            number_of_items=4,
            time="2021-01-16T12:00:00Z"
        )
        expected = 1000
        actual = DeliveryFeeCalculatorHandler()._small_order_fee(order=order, delivery_fee=0)
        self.assertEqual(actual, expected)

    def test_distance_fee(self):
        order = Order(
            cart_value=1000,
            delivery_distance=1000,
            number_of_items=4,
            time="2021-01-16T12:00:00Z"
        )
        expected = 200
        actual = DeliveryFeeCalculatorHandler()._distance_fee(order=order, delivery_fee=0)
        self.assertEqual(actual, expected)

    def test_distance_fee_1(self):
        order = Order(
            cart_value=1000,
            delivery_distance=1001,
            number_of_items=4,
            time="2021-01-16T12:00:00Z"
        )
        expected = 300
        actual = DeliveryFeeCalculatorHandler()._distance_fee(order=order, delivery_fee=0)
        self.assertEqual(actual, expected)

    def test_distance_fee_2(self):
        order = Order(
            cart_value=1000,
            delivery_distance=1500,
            number_of_items=4,
            time="2021-01-16T12:00:00Z"
        )
        expected = 300
        actual = DeliveryFeeCalculatorHandler()._distance_fee(order=order, delivery_fee=0)
        self.assertEqual(actual, expected)

    def test_distance_fee_3(self):
        order = Order(
            cart_value=1000,
            delivery_distance=1501,
            number_of_items=4,
            time="2021-01-16T12:00:00Z"
        )
        expected = 400
        actual = DeliveryFeeCalculatorHandler()._distance_fee(order=order, delivery_fee=0)
        self.assertEqual(actual, expected)

    def test_distance_fee_4(self):
        order = Order(
            cart_value=1000,
            delivery_distance=2000,
            number_of_items=4,
            time="2021-01-16T12:00:00Z"
        )
        expected = 400
        actual = DeliveryFeeCalculatorHandler()._distance_fee(order=order, delivery_fee=0)
        self.assertEqual(actual, expected)

    def test_distance_fee_5(self):
        order = Order(
            cart_value=1000,
            delivery_distance=2001,
            number_of_items=4,
            time="2021-01-16T12:00:00Z"
        )
        expected = 500
        actual = DeliveryFeeCalculatorHandler()._distance_fee(order=order, delivery_fee=0)
        self.assertEqual(actual, expected)

    def test_friday_rush_fee(self):
        order = Order(
            cart_value=1000,
            delivery_distance=1000,
            number_of_items=4,
            time="2023-01-06T15:00:00Z"
        )
        expected = 600
        actual = DeliveryFeeCalculatorHandler()._friday_rush_fee(order=order, delivery_fee=500)
        self.assertEqual(actual, expected)

    def test_friday_rush_fee_1(self):
        order = Order(
            cart_value=1000,
            delivery_distance=1000,
            number_of_items=4,
            time="2023-01-06T14:00:00Z"
        )
        expected = 500
        actual = DeliveryFeeCalculatorHandler()._friday_rush_fee(order=order, delivery_fee=500)
        self.assertEqual(actual, expected)

    def test_friday_rush_fee_2(self):
        order = Order(
            cart_value=1000,
            delivery_distance=1000,
            number_of_items=4,
            time="2023-01-07T15:00:00Z"
        )
        expected = 500
        actual = DeliveryFeeCalculatorHandler()._friday_rush_fee(order=order, delivery_fee=500)
        self.assertEqual(actual, expected)

    def test_friday_rush_fee_3(self):
        order = Order(
            cart_value=1000,
            delivery_distance=1000,
            number_of_items=4,
            time="2023-01-06T19:00:00Z"
        )
        expected = 600
        actual = DeliveryFeeCalculatorHandler()._friday_rush_fee(order=order, delivery_fee=500)
        self.assertEqual(actual, expected)

    def test_friday_rush_fee_4(self):
        order = Order(
            cart_value=1000,
            delivery_distance=1000,
            number_of_items=4,
            time="2023-01-06T20:00:00Z"
        )
        expected = 500
        actual = DeliveryFeeCalculatorHandler()._friday_rush_fee(order=order, delivery_fee=500)
        self.assertEqual(actual, expected)

    def test_free_delivery(self):
        order = Order(
            cart_value=10000,
            delivery_distance=1000,
            number_of_items=4,
            time="2023-01-06T20:00:00Z"
        )
        expected = True
        actual = DeliveryFeeCalculatorHandler()._free_delivery(order=order)
        self.assertEqual(actual, expected)

    def test_free_delivery_1(self):
        order = Order(
            cart_value=9999,
            delivery_distance=1000,
            number_of_items=4,
            time="2023-01-06T20:00:00Z"
        )
        expected = False
        actual = DeliveryFeeCalculatorHandler()._free_delivery(order=order)
        self.assertEqual(actual, expected)

    def test_free_delivery_2(self):
        order = Order(
            cart_value=10001,
            delivery_distance=1000,
            number_of_items=4,
            time="2023-01-06T20:00:00Z"
        )
        expected = True
        actual = DeliveryFeeCalculatorHandler()._free_delivery(order=order)
        self.assertEqual(actual, expected)

    def test_max_fee(self):
        expected = 1500
        actual = DeliveryFeeCalculatorHandler()._max_fee(delivery_fee=1600)
        self.assertEqual(actual, expected)

    def test_max_fee_1(self):
        expected = 1400
        actual = DeliveryFeeCalculatorHandler()._max_fee(delivery_fee=1400)
        self.assertEqual(actual, expected)

    def test_max_fee_2(self):
        expected = 0
        actual = DeliveryFeeCalculatorHandler()._max_fee(delivery_fee=0)
        self.assertEqual(actual, expected)

    def test_handle(self):
        order = Order(
            cart_value=1000,
            delivery_distance=1000,
            number_of_items=4,
            time="2021-01-16T12:00:00Z"
        )
        expected = 200
        actual = DeliveryFeeCalculatorHandler().handle(order=order)
        self.assertEqual(actual, expected)

    def test_handle_1(self):
        order = Order(
            cart_value=1000,
            delivery_distance=1001,
            number_of_items=4,
            time="2021-01-16T12:00:00Z"
        )
        expected = 300
        actual = DeliveryFeeCalculatorHandler().handle(order=order)
        self.assertEqual(actual, expected)

    def test_handle_2(self):
        order = Order(
            cart_value=1000,
            delivery_distance=1500,
            number_of_items=4,
            time="2021-01-16T12:00:00Z"
        )
        expected = 300
        actual = DeliveryFeeCalculatorHandler().handle(order=order)
        self.assertEqual(actual, expected)

    def test_handle_3(self):
        order = Order(
            cart_value=1000,
            delivery_distance=1501,
            number_of_items=4,
            time="2021-01-16T12:00:00Z"
        )
        expected = 400
        actual = DeliveryFeeCalculatorHandler().handle(order=order)
        self.assertEqual(actual, expected)

    def test_handle_4(self):
        order = Order(
            cart_value=1000,
            delivery_distance=2000,
            number_of_items=4,
            time="2021-01-16T12:00:00Z"
        )
        expected = 400
        actual = DeliveryFeeCalculatorHandler().handle(order=order)
        self.assertEqual(actual, expected)

    def test_handle_5(self):
        order = Order(
            cart_value=1000,
            delivery_distance=2001,
            number_of_items=4,
            time="2021-01-16T12:00:00Z"
        )
        expected = 500
        actual = DeliveryFeeCalculatorHandler().handle(order=order)
        self.assertEqual(actual, expected)

    def test_handle_6(self):
        order = Order(
            cart_value=1000,
            delivery_distance=1000,
            number_of_items=4,
            time="2023-01-06T15:00:00Z"
        )
        expected = 240
        actual = DeliveryFeeCalculatorHandler().handle(order=order)
        self.assertEqual(actual, expected)

    def test_handle_7(self):
        order = Order(
            cart_value=10000,
            delivery_distance=1000,
            number_of_items=4,
            time="2023-01-06T15:00:00Z"
        )
        expected = 0
        actual = DeliveryFeeCalculatorHandler().handle(order=order)
        self.assertEqual(actual, expected)

    def test_handle_8(self):
        order = Order(
            cart_value=1000,
            delivery_distance=1000,
            number_of_items=4,
            time="2023-01-06T20:00:00Z"
        )
        expected = 200
        actual = DeliveryFeeCalculatorHandler().handle(order=order)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
