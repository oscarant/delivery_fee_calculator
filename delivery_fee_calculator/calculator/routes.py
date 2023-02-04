from flask import Blueprint, request, jsonify, make_response

calculator_bp = Blueprint("calculator", __name__, url_prefix="/v1")

ENDPOINT_FORMAT = "/calculator/fee"


@calculator_bp.route(ENDPOINT_FORMAT, methods=["POST"])
def calculate_fee():
    return "pong", 200