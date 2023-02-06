from flask import Blueprint, jsonify, Response
from flask_pydantic import validate

from delivery_fee_calculator.calculator.handlers import DeliveryFeeCalculatorHandler
from delivery_fee_calculator.calculator.schemas import Order

calculator_bp = Blueprint("calculator", __name__, url_prefix="/v1")

ENDPOINT_FORMAT = "/calculator/delivery_fee"


@calculator_bp.route(ENDPOINT_FORMAT, methods=["POST"])
@validate()
def calculate_fee(body: Order) -> Response:
    delivery_fee = DeliveryFeeCalculatorHandler().handle(order=body)
    return jsonify({"delivery_fee": delivery_fee})
