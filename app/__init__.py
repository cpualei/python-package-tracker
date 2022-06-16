from flask import Flask, render_template
from .config import Configuration
from .routes import pkg_tracker

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(pkg_tracker.bp)
