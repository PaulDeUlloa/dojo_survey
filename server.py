from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "Ojo_surv12"


# our index route will handle rendering our form
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/users", methods=["POST"])
def create_user():
    print("Succesfully recieved POST info")
    print(request.form)
    session["name"] = request.form["name"]
    session["dojo_location"] = request.form["dojo_location"]
    session["fav_language"] = request.form["fav_language"]
    session["comment"] = request.form["comment"]
    return redirect("/show")


@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template(
        "show.html",
        name_on_template=session["name"],
        location_on_template=session["dojo_location"],
    )


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8010)
