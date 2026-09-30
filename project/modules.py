from .extensions import db
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

