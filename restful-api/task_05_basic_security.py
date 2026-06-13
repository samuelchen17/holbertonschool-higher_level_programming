#!/usr/bin/python3

"""Basic and JWT Auth"""

from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


# Basic auth
# each request is authenticated independently
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)

    if not user and check_password_hash(user["password"], password):
        return user

    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_auth():
    return "Basic Auth: Access Granted"


if __name__ == "__main__":
    app.run()
