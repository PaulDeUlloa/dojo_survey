from flask import render_template, request, redirect, session
from flask_app import app

# "Ojo_surv12"


# our index route will handle rendering our form
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/survey", methods=["POST"])
def create_user():
    print("Succesfully recieved POST info")
    print(request.form)
    session["name"] = request.form["name"]
    session["dojo_location"] = request.form["dojo_location"]
    session["fav_language"] = request.form["fav_language"]
    session["comment"] = request.form["comment"]
    return redirect("/result")


@app.route("/result")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("result.html")


@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8010)
