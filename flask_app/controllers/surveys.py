from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.survey import Survey


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create/survey", methods=["POST"])
def create_survey():
    if Survey.is_valid(request.form):
        Survey.save(request.form)
        return redirect("/results")
    return redirect("/")


# @app.route("/survey", methods=["POST"])
# def create_user():
#     print("Succesfully recieved POST info")
#     print(request.form)
#     session["name"] = request.form["name"]
#     session["dojo_location"] = request.form["dojo_location"]
#     session["fav_language"] = request.form["fav_language"]
#     session["comment"] = request.form["comment"]
#     return redirect("/result")


@app.route("/results")
def results():
    return render_template("results.html", survey=Survey.get_last_survey())


# @app.route("/results")
# def show_user():
#     print("Showing the User Info From the Form")
#     print(request.form)
#     return render_template("results.html")


@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")
