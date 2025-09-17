from netvac.backend.models.user import User

class UserService:
    def register_user(self, username, email, password):
        user = User.create(username, email, password)
        return user

    def get_user_by_username(self, username):
        user = User.find_by_username(username)
        return user