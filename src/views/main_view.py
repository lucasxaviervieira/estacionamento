from flask import Blueprint, request, jsonify
from services.verify_route import token_required

from controllers import SlotController, CarController, OccupationController

bp_main = Blueprint("main", __name__)

slot_controller = SlotController()
car_controller = CarController()
occupation_controller = OccupationController()


@bp_main.route("/slot", methods=["POST"])
@token_required
def create_slot():
    data = request.get_json()
    try:
        response = slot_controller.create_slot(data)
        return jsonify({"data": response}), 200
    except:
        return jsonify({"error": "some error has occured"}), 400


@bp_main.route("/slot", methods=["GET"])
@token_required
def list_slots():
    try:
        slots = slot_controller.get_all_slots()
        return jsonify({"data": slots}), 200
    except:
        return jsonify({"error": "some error has occured"}), 400


@bp_main.route("/car", methods=["POST"])
@token_required
def create_car():
    try:
        data = request.get_json()
        response = car_controller.create_car(data)
        return jsonify(response), 200
    except:
        return jsonify({"error": "some error has occured"}), 400


@bp_main.route("/car", methods=["GET"])
@token_required
def list_cars():
    try:
        cars = car_controller.get_all_cars()
        return jsonify({"data": cars}), 200
    except:
        return jsonify({"error": "some error has occured"}), 400


@bp_main.route("/occupation", methods=["POST"])
@token_required
def create_occupation():
    try:
        data = request.get_json()
        response = occupation_controller.create_occupation(data)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": "some error has occured", "specified": e}), 400


@bp_main.route("/occupation", methods=["GET"])
@token_required
def list_occupations():
    try:
        occupations = occupation_controller.get_all_occupations()
        return jsonify({"data": occupations}), 200
    except Exception as e:
        return jsonify({"error": "some error has occured", "specified": e}), 400
