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
        entry = data.get("entry")
        exit_time = data.get("exit")

        if not all([slot_id, user_id, entry]):
            return {
                "error": "This fields are requireds: 'Slot', 'Car', 'User' and 'Entry'"
            }, 400

        try:
            entry_datetime = datetime.fromisoformat(entry)
            exit_datetime = datetime.fromisoformat(exit_time) if exit_time else None

            new_occupation = Occupation(
                slot_id=slot_id,
                car_id=car_id,
                user_id=user_id,
                entry=entry_datetime,
                exit=exit_datetime,
            )
            db.session.add(new_occupation)
            db.session.commit()
            return {"message": "success"}, 201
        except Exception as e:
            return {"error": str(e)}, 400
