from flask import Blueprint, render_template, session, redirect, url_for
from app.model.models import db, User

role_bp = Blueprint("role", __name__)

@role_bp.route("/select-role")
def select_role():
    session.clear()  # Clear previous session
    return render_template("select_role.html")

@role_bp.route("/continue-as-user")
def continue_as_user():
    session['role'] = 'user'

    # Check if a default user exists, otherwise create one
    user = User.query.filter_by(email="default_user@example.com").first()
    if not user:
        user = User(name="Default User", email="default_user@example.com")
        user.password = "password123"  # default password
        user.save()

    # Store the user ID in session
    session['user_id'] = user.id

    return redirect(url_for('dashboard.lost_items'))
