import hashlib
import json
import os

class Login:
    def __init__(self, app):
        self.app = app

        if not os.path.isfile("Users.json"):
            with open("Users.json", "w") as f:
                f.write("{\n    \n}")
    
    # Main Functions

    def signup(self, username, password):
        users = self.get_users()

        if username in users:
            raise TakenUsername("That username is taken.")
        
        users[username] = {}
        users[username]["password"] = hashlib.sha224(password.encode('utf-8')).hexdigest()
        users[username]["pfp"] = "https://static.thenounproject.com/png/275225-200.png"
        self.app.session["username"] = username
        with open("Users.json", "w") as f:
            json.dump(users, f, indent=4)

    def login(self, username, password):
        users = self.get_users()

        if username in users:
            if users.get(username)["password"] == hashlib.sha224(password.encode("utf-8")).hexdigest():
                self.app.session["username"] = username
            else:
                raise WrongPassword("That password is wrong.")
        else:
            raise BadUsername("That username doesn't exist.")

    def logout(self):
        self.app.session.clear()
    
    # Data Fetching Functions

    def get_users(self):
        with open("Users.json", "r") as f:
            data = json.load(f)
        return data

    def get_user_data(self, username):
        users = self.get_users()
        return users.get(username)

    def logged_in(self):
        try:
            if self.app.session["username"]:
                return True
        except:
            return False
    
    # Data Changing Functions

    def change_username(self, password, new_username):
        users = self.get_users()

        if not self.logged_in():
            raise NotLoggedIn("That browser isn't logged in.")
        username = self.app.session["username"]

        if username == new_username:
            if username in users:
                if users.get(username)["password"] == hashlib.sha224(password.encode("utf-8")).hexdigest():
                    users[username] = new_username
                    with open("Users.json", "w") as f:
                        json.dump(users, f, indent=4)
                else:
                    raise WrongPassword("That password is wrong.")
            else:
                raise TakenUsername("That username is taken.")
        else:
            raise TakenUsername("That user already has that username.")

    def change_password(self, old_password, new_password):
        users = self.get_users()

        if not self.logged_in():
            raise NotLoggedIn("That browser isn't logged in.")
        username = self.app.session["username"]
        
        if users.get(username)["password"] == hashlib.sha224(old_password.encode("utf-8")).hexdigest():
            users[username]["password"] = new_password
            with open("Users.json", "w") as f:
                json.dump(users, f, indent=4)
        else:
            raise WrongPassword("That password is wrong.")

    def change_pfp(self, new_pic):
        users = self.get_users()

        if not self.logged_in():
            raise NotLoggedIn("That browser isn't logged in.")
        
        users[self.app.session["username"]]["pfp"] = new_pic
        with open("Users.json", "w") as f:
            json.dump(users, f, indent=4)

# Errors

class TakenUsername(Exception):
    pass

class BadUsername(Exception):
    pass

class WrongPassword(Exception):
    pass

class NotLoggedIn(Exception):
    pass