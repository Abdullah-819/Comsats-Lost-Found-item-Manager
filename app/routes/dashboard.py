from flask import Blueprint, render_template, session, redirect, url_for, flash

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

@dashboard_bp.route("/")
def dashboard_view():
    if not session.get("user") and not session.get("role"):
        # Guest user (continue as user)
        role = "user"
    else:
        role = session.get("role", "user")

    # Example stats for demo
    stats = {
        "items_lost": 5,
        "items_found": 3,
        "resolved": 2
    }

    return render_template("dashboard.html", role=role, stats=stats)
