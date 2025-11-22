from flask import Blueprint, session, redirect, url_for

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

@dashboard_bp.route("/")
def dashboard():
    if "user" not in session:
        return redirect(url_for("auth.login"))

    return "Dashboard Page (Logged in)"
