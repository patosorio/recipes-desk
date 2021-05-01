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



@app.route("/recipe_info/<recipe_id>")
def recipe_info(recipe_id):
    recipe_data = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe_info.html", recipe=recipe_data)


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


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop('user')
    return redirect(url_for("get_recipes"))



@app.route("/my_recipes/<username>")
def my_recipes(username):
    user_recipes = list(mongo.db.recipes.find(
        {"created_by": session["user"]}))
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("my_recipes.html", username=username, recipes=user_recipes)
        
    return redirect(url_for('login'))



@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":

        # CHECK if recipe exist
        existing_recipe = mongo.db.recipes.find_one(
            {"recipe_name": request.form.get("recipe_name").lower()},
            {"created_by": session["user"]})

        if existing_recipe:
            flash("You have already created a recipe with this exact name.")
        else:
            publish = "yes" if request.form.get("publish") else "no"
            recipe = {
                "recipe_name": request.form.get("recipe_name"),
                "created_by": session["user"],
                "recipe_description": request.form.get("recipe_description"),
                "prep_time": request.form.get("prep_time"),
                "cook_time": request.form.get("cook_time"),
                "servings": request.form.get("servings"),
                "publish": publish,
                "recipe_ingredients": request.form.getlist("recipe_ingredients"),
                "steps": request.form.get("steps")
            }
            mongo.db.recipes.insert_one(recipe)
            flash("Your recipe book has been updated!") 

    return render_template("add_recipe.html")


@app.route("/add_saved/<recipe_id>")
def add_saved(recipe_id):
    mongo.db.users.update(
        {"username": session["user"]},
        {'$addToSet': {"saved": ObjectId(recipe_id)}}
    )
    flash("Added to favorites!")
    return get_recipes()


@app.route("/add_library/<recipe_id>", methods=["GET", "POST"])
def add_library(recipe_id):
    if request.method == "POST":
        mongo.db.libraries.update(
            {"library_name": request.form.get("library_name")},
            {'$addToSet': {"recipes_id": ObjectId(recipe_id)}}
        )
    return get_recipes()


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        publish = "yes" if request.form.get("publish") else "no"
        submit = {
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
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe updated.")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    libraries = mongo.db.libraries.find().sort("library_name", 1)
    return render_template("edit_recipe.html", recipe=recipe, libraries=libraries)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    username = session['user']
    mongo.db.users.update(
        {"username": session['user']},
        {"$pull": {"saved": ObjectId(recipe_id)}})
    flash("Recipe Successfully Deleted")
    return my_recipes(username)
    


@app.route("/my_saved/<username>")
def my_saved(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})
    saved_recipes = username["saved"]
    list_recipes = []
    for saved in saved_recipes:
        list_recipes.append(mongo.db.recipes.find_one(
            {"_id": ObjectId(saved)}))
    return render_template(
        "my_saved.html", username=username, recipes=list_recipes)


# how and where to run:
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
