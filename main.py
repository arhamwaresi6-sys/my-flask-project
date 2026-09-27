from flask import Flask , request,redirect,url_for,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
            name = request.form.get("name")
            return render_template("index.html",name=name)
    return render_template("index.html",name="no name")

@app.route("/form",methods =["GET"])
def form():
    return '''<form action="/" method="POST">
    <input type="text" name="name">
    <button type="submit">Submit</button>
</form>'''

@app.route("/about")
def about():
    return """
    <h1>About</h1>
    <p>This is the about page.</p>
    """


@app.route("/hello/<name>")
def hello(name):
    return f"""
    <h1>Hello, {name}!</h1>
    <p>Welcome to my website.</p>
    """

@app.route("/query")
def query():
    name = request.args.get("name")
    return name


    
@app.route("/result", methods=["POST"])
def result():
    username = request.form.get("username")
    return username
@app.route("/acceptjson", methods=["POST"])
def acceptjson():
    get_json = request.get_json()
    return get_json

@app.route("/old")
def old():
    return redirect(url_for("new"))

@app.route("/new")
def new():
    return "You are now on the new page!"