from flask import Flask, jsonify, request, render_template
import mysql.connector

app=Flask(__name__)

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="flask_app"
)

cursor=db.cursor(dictionary=True)

@app.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html"),200

@app.route("/signup", methods=["GET"])
def signup_page():
    return render_template("signup.html"),200

@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html"),200

@app.route("/api/user", methods=["POST"])
def create_user():
    data = request.get_json()
    return jsonify({
        "status": "User defined",
        "data": data
    }),201

if __name__ == "__main__":
    app.run(debug=True, port=5000)