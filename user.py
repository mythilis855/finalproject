class User:
    def __init__(self, email, name, username, password, role):
        self.email = email
        self.name = name
        self.username = username
        self.password = password
        self.role = role

    def check_role(self, role):
        return self.role == role

    def get_user_info(self):
        return {
            "email": self.email,
            "name": self.name,
            "username": self.username,
            "role": self.role
        }