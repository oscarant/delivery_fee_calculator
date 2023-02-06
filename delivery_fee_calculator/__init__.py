from typing import Any
from flask import Flask, make_response, jsonify, Response
from flask_cors import CORS

from delivery_fee_calculator.exceptions import RequestValidationError

"""
Missing things to do:
- Add tests
- Add error handling
"""


def request_exception_handler(exc: RequestValidationError) -> Response:
    return make_response(jsonify({"validation_error": exc.errors()}), 400)


def init_app(config_file_path: str = "settings.py", **config: Any) -> Flask:
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_pyfile(config_file_path)
    app.config.update(**config)

    """Initialize Plugins """
    CORS(app)

    """Flask context """
    with app.app_context():
        # Include our Routes
        from .calculator import routes as calculator_routes
        from .health import routes as health_routes

        # Register error handlers
        app.register_error_handler(RequestValidationError, request_exception_handler)

        # Register Blueprints
        app.register_blueprint(calculator_routes.calculator_bp)
        app.register_blueprint(health_routes.health_bp)

        return app
