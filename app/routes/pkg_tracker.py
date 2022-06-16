from flask import Blueprint, render_template
from app.shipping_form import ShippingForm

bp = Blueprint("pkg_tracker", __name__, url_prefix="")


@bp.route("/")
def tracker():
    return "<h1>Package Tracker</h1>"


@bp.route("/new_package", methods=["GET", "POST"])
def new_package():
    form = ShippingForm()
    return render_template("shipping_request.html", form=form)
