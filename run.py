import os
#To import the class Flask for the file flask
#To import the function render_template for the file flask
from flask import Flask, render_template

#To crate a instance of the class Flask
app = Flask(__name__)

#To create different route the the menu
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/carreer")
def carreer():
    return render_template("carreer.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)