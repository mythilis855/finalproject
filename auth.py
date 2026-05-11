from pathlib import Path
import json
import uuid
from datetime import datetime

class User:
    def __init__(self, email, name, username, password, role):
        self.email = email
        self.name = name
        self.username = username
        self.password = password
        self.role = role

    def to_dict(self):
        return {
            "email": self.email,
            "name": self.name,
            "username": self.username,
            "password": self.password,
            "role": self.role
        }

class Auth:
    def __init__(self, users_file):
        self.users_file = Path(users_file)
        self.users = self.load_users()

    def load_users(self):
        if self.users_file.exists():
            with open(self.users_file, "r") as f:
                return [User(**user) for user in json.load(f)]
        return []

    def save_users(self):
        with open(self.users_file, "w") as f:
            json.dump([user.to_dict() for user in self.users], f)

    def register(self, email, name, username, password, role):
        if any(u.email == email for u in self.users):
            return "Email already exists!"
        if any(u.username == username for u in self.users):
            return "Username already taken!"

        new_user = User(email, name, username, password, role)
        self.users.append(new_user)
        self.save_users()
        return "Account created! Please login."

    def login(self, username, password, role_guess):
        user = next((u for u in self.users if u.username == username), None)
        if user and user.password == password and user.role == role_guess:
            return user
        return None

    def logout(self):
        return "Logged out successfully!"