import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.errorhandler(404)
def page_not_found(e):
    """
    Displays page not found error
    """
    return redirect(url_for("recipes"))


@app.errorhandler(500)
def internal_server_error(e):
    """
    Displays internal server error
    """
    return render_template("500.html"), 500


@app.errorhandler(403)
def page_note_found(e):
    """
    Displays forbidden page error
    """
    return render_template("403.html"), 403


@app.route("/")
@app.route("/recipes")
def recipes():
    """function finds recipes in db
    renders on page either by search query 
    or categor or all recipes"""

    query = request.args.get("query")
    category = request.args.get("category")
    if query:
        recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    elif category:
        recipes = list(
            mongo.db.recipes.find(
                {"category_name": category}))
    else:
        recipes = list(mongo.db.recipes.find().sort([("_id", -1)]))
    return render_template("recipes.html", query=query, recipes=recipes)


@app.route("/get_recipe/<recipe_id>", methods=["GET", "POST"])
def get_recipe(recipe_id):

    """function finds recipe in db and renders on page"""
    
    recipes = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})
    return render_template('get_recipes.html', recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    """checkes if user exist in db"""
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
        {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        """register user in db"""
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        """check if username exists in db"""
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:

            """ensure hashed password matches user input"""

            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                """invalid password match"""

                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            """username doesn't exist"""

            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    
    """grab the session user's username from db"""

    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    
    """render username profile card"""

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    
    """remove user from session cookie"""

    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    
    """add recipe to db and render flash msg"""

    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_img_URL": request.form.get("recipe_img_URL"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_time": request.form.get("recipe_time"),
            "recipe_serving": request.form.get("recipe_serving"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    
    """function edits recipe and render recipe page"""

    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_img_URL": request.form.get("recipe_img_URL"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_time": request.form.get("recipe_time"),
            "recipe_serving": request.form.get("recipe_serving"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")
        return redirect(url_for('get_recipe', recipe_id=ObjectId(recipe_id)))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    
    """function delets recipe from db"""

    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("recipes"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
