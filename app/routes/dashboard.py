from flask import Blueprint, render_template, session, redirect, url_for, flash

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

@dashboard_bp.route("/")
def dashboard_view():
    if not session.get("user"):
        flash("Please login or continue as user", "danger")
        return redirect(url_for("role.select_role"))

    role = session.get("role", "user")  # Default to user
    # Dummy stats for now
    stats = {
        "items_lost": 5,
        "items_found": 3,
        "resolved": 2
    }

    return render_template("dashboard.html", role=role, stats=stats)
