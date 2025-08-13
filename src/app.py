from flask_cors import CORS
from flask import Flask

from src.config.environment import env
from src.utils.logger import app_logger

import builtins

from src.api.routes import routes_bp


def disable_print(*args, **kwargs):
    """Override fungsi print untuk production"""
    pass


def create_app():
    app = Flask(__name__)
    CORS(app)

    # ===== KONFIGURASI PRODUCTION =====
    if env.FLASK_ENV == 'production':
        # 1. Nonaktifkan semua print()
        builtins.print = disable_print

        # 2. Setup logging yang benar
        app.logger = app_logger

    # Register blueprint
    app.register_blueprint(routes_bp)

    return app


app = create_app()
app.run(host=env.FLASK_HOST, port=env.FLASK_PORT, debug=env.FLASK_DEBUG)
