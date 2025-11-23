from flask import Blueprint, render_template, request, redirect, url_for, flash, session

auth_bp = Blueprint("auth", __name__)

# Admin login route
@auth_bp.route("/admin-login", methods=["GET", "POST"])
def admin_login():
    if session.get("user") and session.get("role") == "admin":
        return redirect(url_for("dashboard.dashboard_view"))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "admin":
            session["user"] = username
            session["role"] = "admin"
            flash("Admin login successful!", "success")
            return redirect(url_for("dashboard.dashboard_view"))
        else:
            flash("Invalid admin credentials", "danger")
    return render_template("admin_login.html")


# ⚠️ Add this logout route
@auth_bp.route("/logout")
def logout():
    session.clear()  # remove all session data
    flash("Logged out successfully.", "success")
    return redirect(url_for("role.select_role"))  # back to role selection page
