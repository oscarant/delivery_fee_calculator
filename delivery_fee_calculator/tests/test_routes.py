import unittest
from delivery_fee_calculator import init_app


class TestAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.app = init_app()
        self.app.testing = True
        self.client = self.app.test_client()

    def test_post_order(self):
        data = {
            "cart_value": 1000,
            "delivery_distance": 1000,
            "number_of_items": 4,
            "time": "2021-01-16T12:00:00Z"
        }
        response = self.client.post('/v1/calculator/delivery_fee', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'delivery_fee': 200})

    def test_post_order_with_small_order_fee(self):
        data = {
            "cart_value": 999,
            "delivery_distance": 1000,
            "number_of_items": 4,
            "time": "2021-01-16T12:00:00Z"
        }
        response = self.client.post('/v1/calculator/delivery_fee', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'delivery_fee': 201})

    def test_post_order_with_distance_fee(self):
        data = {
            "cart_value": 1000,
            "delivery_distance": 1001,
            "number_of_items": 4,
            "time": "2021-01-16T12:00:00Z"
        }
        response = self.client.post('/v1/calculator/delivery_fee', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'delivery_fee': 300})

    def test_post_order_with_time_fee(self):
        data = {
            "cart_value": 1000,
            "delivery_distance": 1000,
            "number_of_items": 4,
            "time": "2021-01-16T17:00:00Z"
        }
        response = self.client.post('/v1/calculator/delivery_fee', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'delivery_fee': 200})

    def test_post_order_with_wrong_time(self):
        data = {
            "cart_value": 1000,
            "delivery_distance": 1000,
            "number_of_items": 4,
            "time": "2021-01-16T12:00:00"
        }
        response = self.client.post('/v1/calculator/delivery_fee', json=data)
        self.assertEqual(response.status_code, 400)

    def test_post_order_with_wrong_cart_value(self):
        data = {
            "cart_value": -1,
            "delivery_distance": 1000,
            "number_of_items": 4,
            "time": "2021-01-16T12:00:00Z"
        }
        response = self.client.post('/v1/calculator/delivery_fee', json=data)
        self.assertEqual(response.status_code, 400)

    def test_post_order_with_wrong_delivery_distance(self):
        data = {
            "cart_value": 1000,
            "delivery_distance": -1,
            "number_of_items": 4,
            "time": "2021-01-16T12:00:00Z"
        }
        response = self.client.post('/v1/calculator/delivery_fee', json=data)
        self.assertEqual(response.status_code, 400)

    def test_post_order_with_wrong_number_of_items(self):
        data = {
            "cart_value": 1000,
            "delivery_distance": 1000,
            "number_of_items": -1,
            "time": "2021-01-16T12:00:00Z"
        }
        response = self.client.post('/v1/calculator/delivery_fee', json=data)
        self.assertEqual(response.status_code, 400)

    def test_post_order_with_wrong_time_format(self):
        data = {
            "cart_value": 1000,
            "delivery_distance": 1000,
            "number_of_items": 4,
            "time": "2021-01-16"
        }
        response = self.client.post('/v1/calculator/delivery_fee', json=data)
        self.assertEqual(response.status_code, 400)

    def test_post_order_with_no_data(self):
        response = self.client.post('/v1/calculator/delivery_fee')
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
