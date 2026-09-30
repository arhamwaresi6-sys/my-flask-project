from flask import Blueprint,redirect,request,render_template,url_for
from .extensions import db
from .modules import Users
main = Blueprint("main",__name__)
@main.route("/form")
def form():
    return render_template("form.html")
@main.route("/create",methods=["POST"])
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





@main.route("/",methods = ["GET","POST"])
# read
def home():
    
    db.create_all()
    users = db.session.execute(db.select(Users)).scalars().all()
    selected_id_list = []
    if request.method == "POST":
        form_string = request.form.get("id")
        selected_id_list = [int(elem) for elem in form_string.split(",") if elem.strip()]
        print(selected_id_list)
    return render_template("index.html",users = users,selected_id_list=selected_id_list,name="Arham")
#update
@main.route("/update",methods=["GET","POST"])
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
@main.route("/delete", methods=["POST"])
def delete():
    data = request.get_json()
    ids = data["ids"]
    db.session.execute(
        db.delete(Users).where(Users.id.in_(ids))
    )

    db.session.commit()

    return {"message": "Deleted successfully"}