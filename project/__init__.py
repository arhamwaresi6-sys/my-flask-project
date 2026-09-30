from flask import Flask
from .extensions import db
from .routes import main
def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()
    db.init_app(app)
    #create all table
    with app.app_context():
        db.create_all()
    app.register_blueprint(main)
    return app
    