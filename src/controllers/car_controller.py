from models import db, Car


class CarController:
    def get_all_cars(self):
        cars = Car.query.all()
        return [car.to_dict() for car in cars]

    def get_car_by_id(self, car_id):
        car = Car.query.get(car_id)
        return car.to_dict() if car else None

    def create_car(self, data):
        lic_plate = data["lic_plate"]
        brand = data["brand"]
        model = data["model"]

        new_car = Car(lic_plate=lic_plate, brand=brand, model=model)
        db.session.add(new_car)
        db.session.commit()
        return new_car.to_dict()
