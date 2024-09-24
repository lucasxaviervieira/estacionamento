from flask import Blueprint, request, jsonify

from controllers.user_controller import UserController


bp_user = Blueprint("user", __name__)

user_controller = UserController()


@bp_user.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    users = user_controller.get_user_by_id(user_id)
    response = {"data": users}
    return jsonify(response)


@bp_user.route("/users", methods=["GET"])
def list_users():
    users = user_controller.get_all_users()
    response = {"data": users}
    return jsonify(response)


@bp_user.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    name = data.get("name")
    username = data.get("username")
    password = data.get("password")

    if not all([name, username, password]):
        return jsonify({"error": "all fields are required"}), 400

    try:
        user_controller.create_user(data)
        return jsonify({"message": "user created successfuly"}), 201
    except:
        return jsonify({"error": "some error as occurred"}), 400


@bp_user.route("/token", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not all([username, password]):
        return (
            jsonify({"error": "This fields are required: 'username' and 'password'"}),
            400,
        )
    try:
        access_token = user_controller.auth(username, password)
        response = {"data": access_token}
        return jsonify(response), 200
    except:
        return jsonify({"error": "some error as occurred"}), 400
