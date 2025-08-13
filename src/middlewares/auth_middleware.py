from flask import request, jsonify
from functools import wraps

from src.database.models import User, RoleEnum
from src.database.connection import SessionLocal
from src.utils.tokenizer import decode_access_token


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        db = None
        try:
            if 'Authorization' in request.headers:
                bearer = request.headers['Authorization']
                token = bearer.split()[1] if bearer.startswith(
                    'Bearer ') else bearer

            if not token:
                return jsonify({"message": "Missing token"}), 401

            data = decode_access_token(token)
            if not data:
                return jsonify({"message": "Invalid or expired token"}), 401

            db = SessionLocal()
            user = db.query(User).filter(User.id == data["user_id"]).first()

            if not user:
                return jsonify({"message": "User not found"}), 404

            request.current_user = user
            return f(*args, **kwargs)

        except Exception as e:
            return jsonify({"message": f"An error occurred: {str(e)}"}), 500

        finally:
            if db:
                db.close()

    return decorated


def admin_required(f):
    @wraps(f)
    @login_required
    def decorated(*args, **kwargs):
        user = request.current_user
        if user.role != RoleEnum.admin:
            return jsonify({"message": "Admin privilege required"}), 403
        return f(*args, **kwargs)
    return decorated
