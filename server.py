from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Surveys stink. Let's move on to something more fun, shall we?"


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/process", methods=["POST"])
def create_user():
    print("Got the info from user!")
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comments"] = request.form["comments"]
    return redirect("/results")


@app.route("/results")
def results():
    return render_template("results.html")

if __name__ == "__main__":
    app.run(debug = True)