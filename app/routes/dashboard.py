from flask import Blueprint, render_template, session, redirect, url_for, flash

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

@dashboard_bp.route("/")
def dashboard_view():
    if not session.get("user"):
        flash("Please login first", "danger")
        return redirect(url_for("auth.login"))

    stats = {
        "items_lost": 0,
        "items_found": 0,
        "resolved": 0
    }
    return render_template("dashboard.html", stats=stats)
