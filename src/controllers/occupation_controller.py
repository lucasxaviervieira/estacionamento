from models import db, Occupation
from datetime import datetime


class OccupationController:
    def get_all_occupations(self):
        occupations = Occupation.query.all()
        return [occupation.to_dict() for occupation in occupations]

    def create_occupation(self, data):
        slot_id = data.get("slot_id")
        car_id = data.get("car_id")
        user_id = data.get("user_id")
        entry = None
        exit = None

        if not all([slot_id, user_id]):
            return {"error": "This fields are required: 'Slot', 'User'"}, 400

        try:
            new_occupation = Occupation(
                slot_id=slot_id, car_id=car_id, user_id=user_id, entry=entry, exit=exit
            )
            db.session.add(new_occupation)
            db.session.commit()
            return {"message": "success"}, 201
        except Exception as e:
            return {"error": str(e)}, 400

    def update_exit(self, occupation_id):
        occupation = Occupation.query.filter_by(id=occupation_id).first()

        if not occupation:
            return {"error": "Occupation not found"}, 404

        try:
            exit_datetime = datetime.now()
            occupation.exit = exit_datetime
            db.session.commit()
            return {"message": "Occupation updated successfully"}, 200
        except Exception as e:
            return {"error": str(e)}, 400
