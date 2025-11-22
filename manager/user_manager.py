class UserManager:

    @staticmethod
    def authenticate(username, password):
        # Temporary static login for testing
        if username == "admin" and password == "admin123":
            return {"username": "admin", "role": "admin"}

        return None
