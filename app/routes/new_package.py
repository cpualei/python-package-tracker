from flask import Flask, Blueprint, render_template, redirect
from app.shipping_form import ShippingForm
from app.models import Package, db
from ..config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)

bp = Blueprint("new_package", __name__, url_prefix="/new_package")


@bp.route("/", methods=["GET", "POST"])
def new_package():
    form = ShippingForm()
    if form.validate_on_submit():
        data = form.data
        new_package = Package(sender=data["sender_name"],
                              recipient=data["recipient_name"],
                              origin=data["origin"],
                              destination=data["destination"],
                              location=data["origin"])
        db.session.add(new_package)
        db.session.commit()
        return redirect("/")
    return render_template("shipping_request.html", form=form)
