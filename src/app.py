from flask import Flask
from models import *
from views.user_view import bp_user
from views.main_view import bp_main
from services.config import Config


app = Flask(__name__)
app.config.from_object(Config)


db.init_app(app)

with app.app_context():
    db.create_all()


app.register_blueprint(bp_user)
app.register_blueprint(bp_main)

if __name__ == "__main__":
    app.run(debug=True)
