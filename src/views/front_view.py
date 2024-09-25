from flask import Blueprint, render_template


bp_front = Blueprint("front", __name__)


@bp_front.route("/login", methods=["GET"])
def login():
    return render_template("front/login/index.html")


@bp_front.route("/index", methods=["GET"])
def occup():
    return render_template("front/occupation/index.html")
