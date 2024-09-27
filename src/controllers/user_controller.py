from models import db, User
from services.security import HashPassword
from services.token import Token

hash = HashPassword()
tk = Token()


class UserController:
    def get_all_users(self):
        users = User.query.all()
        return [user.to_dict() for user in users]

    def get_user_by_id(self, user_id):
        user = User.query.get(user_id)
        return user.to_dict() if user else None

    def get_user_by_username(self, username):
        user = User.query.filter_by(username=username).first()
        return user.to_dict() if user else None

    def create_user(self, data, role="normal"):
        name = data["name"]
        username = data["username"]
        password = data["password"]

        hashed_password = hash.hash_password(password)

        new_user = User(
            name=name, username=username, password=hashed_password, role=role
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict()

    def auth(self, inp_username, inp_password):
        stored_user = self.get_user_by_username(inp_username)
        stored_password = stored_user["password"]

        verify_password = hash.verify_password(stored_password, inp_password)

        if verify_password:
            try:
                stored_user_id = stored_user["id"]
                token = tk.provide_token(stored_user_id)
                return token
            except Exception as error:
                return error
        else:
            return {"message": "User not found"}
