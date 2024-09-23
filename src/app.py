from flask import Flask
from models import db
from views.user_view import bp_user
from services.config import Config

app = Flask(__name__)
app.config.from_object(Config)


db.init_app(app)

with app.app_context():
    db.create_all()


app.register_blueprint(bp_user)

if __name__ == "__main__":
    app.run(debug=True)
