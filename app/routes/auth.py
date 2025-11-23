from flask import Blueprint, render_template, request, redirect, url_for, flash, session

auth_bp = Blueprint("auth", __name__, url_prefix="")  # no template_folder needed if using app/templates

# Temporary user storage
USERS = {"admin": "admin"}  # username: password

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    # Redirect logged-in users to dashboard
    if session.get("user"):
        return redirect(url_for("dashboard.dashboard_view"))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if USERS.get(username) == password:
            session["user"] = username
            flash("Login successful!", "success")
            return redirect(url_for("dashboard.dashboard_view"))
        else:
            flash("Invalid username or password", "danger")

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully.", "success")
    return redirect(url_for("auth.login"))
