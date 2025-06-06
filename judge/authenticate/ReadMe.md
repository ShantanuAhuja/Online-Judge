<h1>Authentication Overview</h1>
This project implements a secure authentication system using Django's built-in authentication tools. The system supports the following features:

<h2>Signup</h2>
Users can register by providing their first name, last name, username, and password.

The system ensures that passwords match and checks if the username is already taken before creating a new user.

<h2>Login</h2>
Users can log in by entering their username and password.

If the username exists and the password is correct, the user is authenticated and logged in.

In case of an incorrect username or password, appropriate error messages are displayed.

<h2>Logout</h2>
Users can log out, which ends their session and redirects them to the login page.

<h2>Security</h2>
Passwords are securely hashed using Django’s set_password method.

Authentication is handled using Django's built-in authenticate and login methods to ensure the security of user sessions.
