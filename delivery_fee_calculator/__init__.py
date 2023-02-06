from typing import Any
from flask import Flask
from flask_cors import CORS

"""
Missing things to do:
- Add tests
- Add more comments
"""


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

        # Register Blueprints
        app.register_blueprint(calculator_routes.calculator_bp)
        app.register_blueprint(health_routes.health_bp)

        return app
