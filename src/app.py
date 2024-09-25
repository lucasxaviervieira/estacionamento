from flask import Flask
from models import *
from views import *
from services.config import Config


app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.config.from_object(Config)


db.init_app(app)

with app.app_context():
    db.create_all()


app.register_blueprint(bp_user)
app.register_blueprint(bp_main)
app.register_blueprint(bp_swagger)

if __name__ == "__main__":
    app.run(debug=True)
