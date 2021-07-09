# EZ-Login
## Description
EZ-Login is a cool Flask extension that allows users to signup, login, logout, and more!

## Documentation
### Installation
Enter the following into your Command Line:
```sh
cd /dir/to/project/
git clone https://github.com/uberBuilder24/EZ-Login
pip install -r requirement.txt
```
After you download the source code, you you need to import the library. To do so, add `import flask` and `import EZLogin` to the top of your Python file. Make sure the `EZLogin.py` file and the file you wish to use the library in are in the same directory. To initialize the library, add the following code after your imports.
```py
app = Flask(__name__)
app.secret_key = "Replace this with random letters..."
loginManager = EZLogin.Login()
```
After you have that code, create a `Users.json` file. If you put the file in a different directory from your `login.py` file, add the following to your code.
```py
loginManager.data_folder = "./path/to/data/folder/"
```

### Functions
#### Main Functions
`loginManager.signup(username, password)` - Creates a new user.

`loginManager.login(username, password)` - Signs a user in.

`loginManager.logout()` - Signs a user out.

#### Data Fetching Functions
`loginManager.get_users()` - Returns all the users.

`loginManager.get_user_data(username)` - Return data on a specific user.

`loginManager.logged_in()` - Returns whether a browser is logged in.

#### Data Changing Functions
`loginManager.change_username(password, new_username)` - Changes a user's username.

`loginManager.change_password(old_password, new_password)` - Changes a user's password.

`loginManager.change_pfp(new_pic)` - Changes a user's profile picture.

### Errors
```
TakenUsername
BadUsername
WrongPassword
NotLoggedIn
```