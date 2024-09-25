from flask import Blueprint, render_template


bp_swagger = Blueprint("swagger", __name__)


@bp_swagger.route("/", methods=["GET"])
def init_swagger():
    return render_template("swagger/index.html")
