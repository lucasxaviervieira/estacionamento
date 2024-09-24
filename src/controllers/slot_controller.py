from models import db, Slot


class SlotController:
    def get_all_slots(self):
        slots = Slot.query.all()
        return [slot.to_dict() for slot in slots]

    def get_slot_by_id(self, slot_id):
        slot = Slot.query.get(slot_id)
        return slot.to_dict() if slot else None

    def create_slot(self, data):
        number = data["number"]
        floor = data["floor"]

        code = f"{number}_{floor}"

        new_slot = Slot(code=code, number=number, floor=floor)
        db.session.add(new_slot)
        db.session.commit()
        return new_slot.to_dict()
