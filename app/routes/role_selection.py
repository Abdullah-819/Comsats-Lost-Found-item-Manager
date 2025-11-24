from flask import Blueprint, render_template, session, redirect, url_for

role_bp = Blueprint("role", __name__)

@role_bp.route("/select-role")
def select_role():
    # Clear session when returning to role selection
    session.clear()
    return render_template("select_role.html")


@role_bp.route("/continue-as-user")
def continue_as_user():
    # Set role to 'user' in session
    session['role'] = 'user'
    # Redirect user directly to Lost Items page
    return redirect(url_for('dashboard.lost_items'))
