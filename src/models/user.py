from models import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(125), nullable=False)
    username = db.Column(db.String(125), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(
        db.String(6),
        nullable=False,
        default="normal",
    )

    def __init__(self, name, username, password, role="normal"):
        self.name = name
        self.username = username
        self.password = password
        self.role = role

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "password": self.password,
            "role": self.role,
        }
