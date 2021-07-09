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
After you download the source code, you you need to import the library. To do so, add `import flask` and `import EZLogin` to the top of your Python file. Make sure the `EZLogin.py` file and the file you wish to use the library in are in the same directory. To initialize the library, add the following code after your imports.
```py
app = Flask(__name__)
app.secret_key = "Secret"
loginManager = EZLogin.Login()
```

### Functions
#### Main Functions
`signup(username, password)` - Creates a new user.
`login(username, password)` - Signs a user in.
`logout()` - Signs a user out.

#### Data Fetching Functions
`get_users()` - Returns all the users.
`get_user_data(username)` - Return data on a specific user.
`logged_in()` - Returns whether a browser is logged in.

#### Data Changing Functions
`change_username(password, new_username)` - Changes a user's username.
`change_password(old_password, new_password)` - Changes a user's password.
`change_pfp(new_pic)` - Changes a user's profile picture.