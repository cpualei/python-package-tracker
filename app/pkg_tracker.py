from flask import Blueprint

bp = Blueprint("pkg_tracker", __name__, url_prefix="")

@bp.route("/")
def tracker():
    return "<h1>Package Tracker</h1>"
