#!/usr/bin/python3

"""This module contains a flask app"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)

    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    user = request.get_json(silent=True)

    if user is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = user.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = user

    return (
        jsonify(
            {
                "message": "User added",
                "user": user,
            }
        ),
        201,
    )


if __name__ == "__main__":
    app.run()
