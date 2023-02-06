from flask import Blueprint, request, jsonify
from pydantic import ValidationError

from delivery_fee_calculator.calculator.handlers import DeliveryFeeCalculatorHandler
from delivery_fee_calculator.calculator.schemas import Order

calculator_bp = Blueprint("calculator", __name__, url_prefix="/v1")

ENDPOINT_FORMAT = "/calculator/delivery_fee"


@calculator_bp.route(ENDPOINT_FORMAT, methods=["POST"])
def calculate_fee():
    try:
        order = Order(**request.json)
    except ValidationError as e:
        return jsonify(e.errors()), 400
    delivery_fee = DeliveryFeeCalculatorHandler().handle(order=order)
    return jsonify({"delivery_fee": delivery_fee})
