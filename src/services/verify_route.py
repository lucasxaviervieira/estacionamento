from functools import wraps
from flask import request, jsonify
from services.token import Token


token_service = Token()


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]

            token = auth_header.split(" ")[1] if len(auth_header.split()) == 2 else None

        if not token:
            return jsonify({"message": "Token needed"}), 401

        decoded_token = token_service.decode_access_token(token)

        if "error" in decoded_token:
            return jsonify({"message": decoded_token["error"]}), 401

        return f(*args, **kwargs)

    return decorated
