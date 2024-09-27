from flask_sqlalchemy import SQLAlchemy
from collections import OrderedDict
from datetime import datetime

db = SQLAlchemy()


class Slot(db.Model):
    __tablename__ = "slot"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(12), unique=True, nullable=False)
    number = db.Column(db.String(3), nullable=False)
    floor = db.Column(db.String(1), nullable=False)

    def __init__(self, code, number, floor):
        self.code = code
        self.number = number
        self.floor = floor

    def to_dict(self):
        return OrderedDict(
            {
                "id": self.id,
                "code": self.code,
                "number": self.number,
                "floor": self.floor,
            }
        )


class Car(db.Model):
    __tablename__ = "car"

    id = db.Column(db.Integer, primary_key=True)
    lic_plate = db.Column(db.String(7), unique=True, nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)

    def __init__(self, lic_plate, brand, model):
        self.lic_plate = lic_plate
        self.brand = brand
        self.model = model

    def to_dict(self):
        return OrderedDict(
            {
                "id": self.id,
                "lic_plate": self.lic_plate,
                "brand": self.brand,
                "model": self.model,
            }
        )


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(125), nullable=False)
    username = db.Column(db.String(125), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(6), nullable=False, default="normal")

    def __init__(self, name, username, password, role="normal"):
        self.name = name
        self.username = username
        self.password = password
        self.role = role

    def to_dict(self):
        return OrderedDict(
            {
                "id": self.id,
                "name": self.name,
                "username": self.username,
                "password": self.password,
                "role": self.role,
            }
        )


class Occupation(db.Model):
    __tablename__ = "occupation"

    id = db.Column(db.Integer, primary_key=True)
    slot_id = db.Column(db.Integer, db.ForeignKey("slot.id"), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey("car.id"), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    entry = db.Column(
        db.DateTime(timezone=True), nullable=False, default=datetime.utcnow
    )
    exit = db.Column(db.DateTime(timezone=True), nullable=True)

    slot = db.relationship("Slot", backref=db.backref("occupations", lazy=True))
    car = db.relationship("Car", backref=db.backref("occupations", lazy=True))
    user = db.relationship("User", backref=db.backref("occupations", lazy=True))

    def __init__(self, slot_id, car_id, user_id, entry, exit):
        self.slot_id = slot_id
        self.car_id = car_id
        self.user_id = user_id
        self.entry = entry
        self.exit = exit

    def to_dict(self):
        return OrderedDict(
            {
                "id": self.id,
                "slot": {
                    "id": self.slot.id,
                    "code": self.slot.code,
                    "number": self.slot.number,
                    "floor": self.slot.floor,
                },
                "car": {
                    "id": self.car.id if self.car else None,
                    "lic_plate": self.car.lic_plate if self.car else None,
                    "brand": self.car.brand if self.car else None,
                    "model": self.car.model if self.car else None,
                },
                "user": {
                    "id": self.user.id,
                    "name": self.user.name,
                    "username": self.user.username,
                },
                "entry": self.entry.isoformat() if self.entry else None,
                "exit": self.exit.isoformat() if self.exit else None,
            }
        )
