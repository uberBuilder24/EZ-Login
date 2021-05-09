# EZ-Login
## Description
EZ-Login is a cool Flask extension that allows users to signup, login, logout, and more!

## Documentation
### Installation
Enter the following into your Command Line:
```sh
cd /dir/to/project/
git clone https://github.com/uberBuilder24/EZ-Login
```
After you download the source code, you you need to import the library. To do so, add `import flask` and `import login` to the top of your Python file. Make sure the `login.py` file and the file you wish to use the library in are in the same directory. To initialize the library, add the following code after your imports.
```py
app = Flask(__name__)
app.secret_key = "Secret"
loginManager = login.Login()
```

### Functions
`loginManager.signup(username, password)` - This will create a user in the JSON.

`loginManager.login(username, password)` - This will login a already-existing user.

`loginManager.logged_in()` - This will return a bool (True or False) containing whether or not the user is logged in.

`loginManager.logout()` - This will logout the current user.

`loginManager.get_users()` - This will return a dictionary object containing all the users.

`loginManager.get_user_data(user_id)` - This will return the data for a specific user.

### Errors
Each error has it's own string:

`"AE"` - Username Already Exixts. (`Signup` function).

`"IU"` - Invalid Username. (`Login` function).

`"IP"` - Invalid Password. (`Login` function).

However, if the `signup` or `login` function return `True`, the action was successful.