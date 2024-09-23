from werkzeug.security import generate_password_hash, check_password_hash


class HashPassword:

    def __init__(self):
        self.method = "pbkdf2:sha256"
        self.salt_length = 16

    def hash_password(self, password):
        return generate_password_hash(
            password, method=self.method, salt_length=self.salt_length
        )

    def verify_password(self, stored_password_hash, password):
        return check_password_hash(stored_password_hash, password)
