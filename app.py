import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask("__name__")

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    libraries = mongo.db.libraries.find().sort("library_name", 1)
    return render_template(
        "recipes.html", recipes=recipes, libraries=libraries)


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        # CHECK if user exist
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user or existing_email:
            flash("This email or username already exists!")
            return redirect(url_for("sign_up"))

        # if the user doesn't exist, create a dictionary to insert in database
        new_user = {
            "username": request.form.get("username").lower(),
            "fname": request.form.get("fname").lower(),
            "lname": request.form.get("lname").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email").lower()
        }
        mongo.db.users.insert_one(new_user)

        # new user to session cookie
        session["user"] = request.form.get("username").lower()
        flash("Welcome to Rec!pe-Desk!")
    return render_template("sign_up.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check password hash
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                # set session cookie to the current user
                session['user'] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for('my_recipes', username=session['user']))         
            else:
                # invalid password 
                flash("Incorrect password or username.")
                return redirect(url_for('login'))       
        
        else:
            # username doesn't exist
            flash("Incorrect password or username.")
            return redirect(url_for('login'))

    return render_template("login.html")


@app.route("/my_recipes/<username>", methods=["GET", "POST"])
def my_recipes(username):
    user_recipes = list(mongo.db.recipes.find(
        {"created_by": session["user"]}))
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("my_recipes.html", username=username, recipes=user_recipes)
        
    return redirect(url_for('login'))


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop('user')
    return redirect(url_for("get_recipes"), recipes=recipes)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        publish = "yes" if request.form.get("publish") else "no"
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "created_by": session["user"],
            "recipe_description": request.form.get("recipe_description"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "servings": request.form.get("servings"),
            "publish": publish,
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "steps": request.form.get("steps")
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Your recipe book has been updated!")    
        return redirect(url_for('my_recipes', username=session['user']))

    return render_template("add_recipe.html")


@app.route("/add_saved/<recipe_id>")
def add_saved(recipe_id):
    mongo.db.users.update(
        {"username": session["user"]},
        {'$addToSet': {"saved": ObjectId(recipe_id)}}
    )
    return redirect(url_for("get_recipes"))


@app.route("/add_library/<recipe_id>")
def add_library(recipe_id): 
    mongo.db.libraries.update(
        {"library_name": request.form.get("library_name")},
        {'$addToSet': {"saved": ObjectId(recipe_id)}}
    )
    return redirect(url_for("get_recipes"))


# how and where to run:
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
