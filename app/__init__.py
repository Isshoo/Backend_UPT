from flask_cors import CORS
from flask import Flask

from app.config import FLASK_ENV, FLASK_DEBUG, FLASK_HOST, FLASK_PORT
from app.utils.logger import app_logger

import builtins

from app.api.routes import routes_bp


def disable_print(*args, **kwargs):
    """Override fungsi print untuk production"""
    pass


def create_app():
    app = Flask(__name__)
    CORS(app)

    # ===== KONFIGURASI PRODUCTION =====
    if FLASK_ENV == 'production':
        # 1. Nonaktifkan semua print()
        builtins.print = disable_print

        # 2. Setup logging yang benar
        app.logger = app_logger

    # Register blueprint
    app.register_blueprint(routes_bp)

    return app


app = create_app()
app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)
