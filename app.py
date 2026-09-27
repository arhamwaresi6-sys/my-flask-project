from flask import Flask , request,redirect,url_for,render_template
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=os.getenv("DATABASE_URL")
db = SQLAlchemy(app)
class Users(db.Model):
    id = db.Column(db.Integer,autoincrement = True, primary_key = True)
    name = db.Column(db.String(100),nullable = False)
    email = db.Column(db.String(100),nullable = False,unique = True)
    gender = db.Column(db.Enum("male","female","other"),nullable = False)
    birth_date = db.Column(db.Date)
    salary = db.Column(db.Numeric(10,2))
    created_at = db.Column(db.TIMESTAMP,
                           server_default = db.func.current_timestamp()
                           )


#Create
@app.route("/form")
def form():
    return render_template("form.html")
@app.route("/create",methods=["POST"])
def create():
    form = request.form
    name = form.get("name")
    email = form.get("email")
    gender = form.get("gender")
    birth_date = form.get("birth_date")
    salary = form.get("salary")
    user = Users(
        name = name,
        email = email,
        gender = gender,
        birth_date = birth_date,
        salary = salary
    )
    db.session.add(user)
    db.session.commit()
    return redirect(url_for("home"))





@app.route("/",methods = ["GET","POST"])
# read
def home():
    
    db.create_all()
    users = db.session.execute(db.select(Users)).scalars().all()
    selected_id_list = []
    if request.method == "POST":
        form_string = request.form.get("id")
        selected_id_list = [int(elem) for elem in form_string.split(",") if elem.strip()]
        print(selected_id_list)
    return render_template("index.html",users = users,selected_id_list=selected_id_list)
#update
@app.route("/update",methods=["GET","POST"])
def update():

    if request.method == "POST":
        form = request.form

        id = form.get("id")
        name = form.get("name")
        email = form.get("email")
        gender = form.get("gender")
        birth_date = form.get("birth_date")
        salary = form.get("salary")

        user = db.session.get(Users, id)

        user.name = name
        user.email = email
        user.gender = gender
        user.birth_date = birth_date
        user.salary = salary

        db.session.commit()

        return redirect(url_for("home"))
    return render_template("update.html")

#delete
@app.route("/delete", methods=["POST"])
def delete():
    data = request.get_json()
    ids = data["ids"]
    db.session.execute(
        db.delete(Users).where(Users.id.in_(ids))
    )

    db.session.commit()

    return {"message": "Deleted successfully"}