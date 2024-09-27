from functools import wraps
from flask import request, jsonify
from services.token import Token
from controllers.user_controller import UserController


token_service = Token()
user_controller = UserController()


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]

            token = auth_header.split(" ")[1] if len(auth_header.split()) == 2 else None

        if not token:
            return jsonify({"message": "Token is missing"}), 401

        decoded_token = token_service.decode_access_token(token)

        if "error" in decoded_token:
            return jsonify({"message": decoded_token["error"]}), 401

        return f(*args, **kwargs)

    return decorated


def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]

        if not token:
            return jsonify({"message": "Token is missing!"}), 401

        try:
            decoded_token = token_service.decode_access_token(token)

            current_user = user_controller.get_user_by_id(decoded_token["sub"])

            if current_user.role != "admin":
                return jsonify({"message": "Admin access required!"}), 403

        except Exception as e:
            return jsonify({"message": "Token is invalid!", "error": str(e)}), 401

        return f(current_user, *args, **kwargs)

    return decorated
