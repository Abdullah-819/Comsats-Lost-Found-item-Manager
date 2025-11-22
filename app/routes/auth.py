from flask import Blueprint, render_template, request, redirect, session, url_for
from app.manager.user_manager import UserManager

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        user = UserManager.authenticate(
            request.form["username"],
            request.form["password"]
        )

        if user:
            session["user"] = user  # save login session
            return redirect(url_for("dashboard.dashboard"))
        else:
            error = "Invalid username or password."

    return render_template("login.html", error=error)


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
