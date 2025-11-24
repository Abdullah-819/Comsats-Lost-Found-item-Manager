from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from app.model.models import db, LostItem, FoundItem, User
from app.manager.item_manager import get_lost_items, get_found_items
import os
from werkzeug.utils import secure_filename

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# -----------------------------
# Main Dashboard
# -----------------------------
@dashboard_bp.route("/")
def dashboard_view():
    role = session.get("role", "user")
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
        file = request.files.get("image_file")
        user_id = session.get("user_id")

        if not user_id:
            flash("User not logged in properly.", "danger")
            return redirect(url_for("dashboard.lost_items"))

        filename = ""
        if file and allowed_file(file.filename):
            filename_secure = secure_filename(file.filename)
            save_path = os.path.join(current_app.root_path, UPLOAD_FOLDER)
            os.makedirs(save_path, exist_ok=True)
            file.save(os.path.join(save_path, filename_secure))
            filename = f"uploads/{filename_secure}"
        elif file:
            flash("Invalid image file type!", "warning")

        new_item = LostItem(
            name=name,
            description=description,
            location=location,
            contact=contact,
            image_url=filename,
            submitted_by_user=user_id
        )
        new_item.save()
        flash("Item uploaded successfully!", "success")
        return redirect(url_for("dashboard.lost_items"))

    return render_template("upload_item.html")
