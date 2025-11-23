from flask import Blueprint, render_template

role_bp = Blueprint("role", __name__)

@role_bp.route("/select-role")
def select_role():
    return render_template("select_role.html")
