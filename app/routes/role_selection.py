from flask import Blueprint, render_template, session, redirect, url_for, flash

role_bp = Blueprint("role", __name__)

@role_bp.route("/select-role")
def select_role():
    # Optional: clear session when returning to role selection
    session.clear()
    return render_template("select_role.html")
