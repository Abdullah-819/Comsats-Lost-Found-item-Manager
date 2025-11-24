from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.model.models import db, LostItem, FoundItem, User
from app.manager.item_manager import get_lost_items, get_found_items

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

# -----------------------------
# Main Dashboard
# -----------------------------
@dashboard_bp.route("/")
def dashboard_view():
    role = session.get("role", "user")  # default = user

    stats = {
        "items_lost": len(get_lost_items()),
        "items_found": len(get_found_items()),
        "resolved": sum(1 for i in get_lost_items() if i.status=="resolved")
    }

    return render_template("dashboard.html", role=role, stats=stats)


# -----------------------------
# Lost Items Page
# -----------------------------
@dashboard_bp.route("/lost")
def lost_items():
    role = session.get("role", "user")
    items = get_lost_items()
    return render_template("lost_items.html", items=items, role=role)


# -----------------------------
# Found Items Page
# -----------------------------
@dashboard_bp.route("/found")
def found_items():
    role = session.get("role", "user")
    items = get_found_items()
    return render_template("found_items.html", items=items, role=role)


# -----------------------------
# User Upload Lost Item
# -----------------------------
@dashboard_bp.route("/upload_item", methods=["GET", "POST"])
def upload_item():
    if session.get("role") != "user":
        flash("Only regular users can upload items.", "danger")
        return redirect(url_for("dashboard.lost_items"))

    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        location = request.form.get("location")
        contact = request.form.get("contact")
        image_url = request.form.get("image_url")  # for now, just text input
        user_id = session.get("user_id")  # must be set on login

        if not user_id:
            flash("User not logged in properly.", "danger")
            return redirect(url_for("dashboard.lost_items"))

        new_item = LostItem(
            name=name,
            description=description,
            location=location,
            contact=contact,
            image_url=image_url,
            submitted_by_user=user_id
        )
        new_item.save()
        flash("Item uploaded successfully!", "success")
        return redirect(url_for("dashboard.lost_items"))

    return render_template("upload_item.html")
