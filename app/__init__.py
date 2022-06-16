from flask import Flask, render_template
from .config import Configuration
from .pkg_tracker import bp

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(bp)
