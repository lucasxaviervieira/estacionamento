from models.user import db, User
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

    def create_user(self, data):
        name = data["name"]
        username = data["username"]
        password = data["password"]
        role = "normal"

        hashed_password = hash.hash_password(password)

        new_user = User(
            name=name, username=username, password=hashed_password, role=role
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict()

    def auth(self, data):
        inp_username = data["username"]
        inp_password = data["password"]

        stored_user = self.get_user_by_username(inp_username)
        stored_password = stored_user["password"]

        verify_password = hash.verify_password(stored_password, inp_password)

        if verify_password:
            try:
                stored_user_id = stored_user["id"]
                auth = tk.auth(stored_user_id)
                return auth
            except Exception as error:
                return error
        else:
            return {"message": "User not found"}

    def verify_access_token(self, token):
        return tk.decode_access_token(token)
