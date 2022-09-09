from flask import Flask, render_template, request
from sources.config import db_connect as db

import pymongo

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config['SECRET_KEY'] = 'any secret key'

# checklst database collections
database = db
coll_users = database.users

@app.route("/")
def index():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form["username"]
    password = request.form["password"]

    user = coll_users.find_one({"username": username})
    
    # user does not exist
    if not(user):
        return {"success": False, "message": "Email doesn't exist in database.", "emailError": True}, 404

    # check if password match with db
    if password != user["password"]:
        return {"success": False, "message": "Invalid email and password combination", "emailError": True}, 401

 
    return render_template("dashboard.html", user=user)

if __name__ == '__main__':
    # HOST = "0.0.0.0"
    # PORT = 5000

    # httpserver.serve(app, host=HOST, port=PORT)
    app.run(port=5000, debug=True)
