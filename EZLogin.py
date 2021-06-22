from flask import Flask, session
import json
import hashlib
import os

app = Flask(__name__)
app.secret_key = "Secret"

class Login:
    def __init__(self):
        if not os.path.isfile("Users.json"):
            with open("Users.json", "w") as f:
                f.write("{\n    \n}")

    def signup(self, username, password):
        users = self.get_users()

        for user in users:
            if users.get(user)["username"] == username:
                return "AE"
        
        lastId = len(users) + 1

        users[str(lastId)] = {}
        users[str(lastId)]["username"] = username
        users[str(lastId)]["password"] = hashlib.sha224(password.encode('utf-8')).hexdigest()
        with open("Users.json", "w") as f:
            json.dump(users, f, indent=4)
        
        return True

    def login(self, username, password):
        users = self.get_users()

        for user in users:
            if users.get(user)["username"] == username:
                if users.get(user)["password"] == hashlib.sha224(password.encode('utf-8')).hexdigest():
                    session["id"] = user
                    return True
                else:
                    return "IP"
        
        return "IU"
    
    def logged_in(self):
        try:
            if session["id"]:
                return True
        except:
            return False

    def logout(self):
        session.clear()

    def get_users(self):
        with open("Users.json", "r") as f:
            data = json.load(f)
        return data
    
    def get_user_data(self, user_id):
        users = self.get_users()
        return users.get(str(user_id))