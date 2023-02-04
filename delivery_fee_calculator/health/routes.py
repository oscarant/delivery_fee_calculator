from typing import Tuple

from flask import Blueprint


health_bp = Blueprint("health", __name__)


@health_bp.route("/-/ping")
def ping() -> Tuple[str, int]:
    """
    This might be seen as silly at this moment, but the goal is to respond with more
    info as the service grows. For example, check connectivity to the DB or some
    other critical dependency
    """
    return "pong", 200
