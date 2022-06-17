from flask import Flask, render_template
from flask_migrate import Migrate
from .config import Configuration
from .routes import pkg_tracker, new_package
from .models import db

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(pkg_tracker.bp)
app.register_blueprint(new_package.bp)
db.init_app(app)
migrate = Migrate(app, db)
