import jwt
import os
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

load_dotenv()


class Token:
    def __init__(self):
        self.SECRET_KEY = os.getenv("SECRET_KEY")

    def auth(self, user_id):
        access_token = self.encode_access_token(user_id)
        auth_obj = {"access_token": access_token}
        return auth_obj

    def encode_token(self, sub, expires_sec):
        try:
            payload = {
                "exp": datetime.now(tz=timezone.utc) + timedelta(seconds=expires_sec),
                "iat": datetime.now(tz=timezone.utc),
                "sub": sub,
            }
            return jwt.encode(payload, self.SECRET_KEY, algorithm="HS256")
        except Exception as e:
            return {"error": f"Token generation error: {str(e)}"}

    def encode_access_token(self, user_id):
        expires_sec = 900  # 900 | 15 min
        access_token = self.encode_token(user_id, expires_sec)
        return access_token

    def decode_access_token(self, access_token):
        try:
            payload = jwt.decode(access_token, self.SECRET_KEY, algorithms="HS256")
            return payload
        except jwt.ExpiredSignatureError:
            message_error = "Signature expired. Please log in again."
            return {"error": message_error}
        except jwt.InvalidTokenError:
            message_error = "Invalid token. Please log in again."
            return {"error": message_error}
