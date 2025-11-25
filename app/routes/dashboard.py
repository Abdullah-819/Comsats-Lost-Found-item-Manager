from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from app.model.models import db, LostItem, FoundItem
from app.manager.item_manager import get_lost_items, get_found_items
from werkzeug.utils import secure_filename
import os

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# -----------------------------
# Dashboard
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
# Lost Items
# -----------------------------
@dashboard_bp.route("/lost")
def lost_items():
    role = session.get("role", "user")
    items = get_lost_items()
    return render_template("lost_items.html", items=items, role=role)

# -----------------------------
# Found Items
# -----------------------------
@dashboard_bp.route("/found")
def found_items():
    role = session.get("role", "user")
    items = get_found_items()
    return render_template("found_items.html", items=items, role=role)

# -----------------------------
# Add Item (Admin & User)
# -----------------------------
@dashboard_bp.route("/add_item", methods=["GET", "POST"])
def add_item():
    role = session.get("role", "user")
    if request.method == "POST":
        item_type = request.form.get("item_type")  # lost or found
        name = request.form.get("name")
        description = request.form.get("description")
        location = request.form.get("location")
        contact = request.form.get("contact")
        file = request.files.get("image_file")
        user_id = session.get("user_id") if role == "user" else None

        filename = ""
        if file and allowed_file(file.filename):
            filename_secure = secure_filename(file.filename)
            save_path = os.path.join(current_app.root_path, UPLOAD_FOLDER)
            os.makedirs(save_path, exist_ok=True)
            file.save(os.path.join(save_path, filename_secure))
            filename = f"uploads/{filename_secure}"
        elif file:
            flash("Invalid image file type!", "warning")

        if item_type == "lost":
            new_item = LostItem(name=name, description=description, location=location,
                                contact=contact, image_url=filename, submitted_by_user=user_id)
        else:
            new_item = FoundItem(name=name, description=description, location=location,
                                 contact=contact, image_url=filename, submitted_by_user=user_id)

        new_item.save()
        flash(f"{item_type.capitalize()} item added successfully!", "success")
        return redirect(url_for(f"dashboard.{item_type}_items"))

    return render_template("add_edit_item.html", role=role, action="Add")

# -----------------------------
# Edit Item
# -----------------------------
@dashboard_bp.route("/edit_item/<string:item_type>/<int:item_id>", methods=["GET", "POST"])
def edit_item(item_type, item_id):
    role = session.get("role", "user")
    if item_type == "lost":
        item = LostItem.query.get_or_404(item_id)
    else:
        item = FoundItem.query.get_or_404(item_id)

    if request.method == "POST":
        item.name = request.form.get("name")
        item.description = request.form.get("description")
        item.location = request.form.get("location")
        item.contact = request.form.get("contact")
        file = request.files.get("image_file")

        if file and allowed_file(file.filename):
            filename_secure = secure_filename(file.filename)
            save_path = os.path.join(current_app.root_path, UPLOAD_FOLDER)
            os.makedirs(save_path, exist_ok=True)
            file.save(os.path.join(save_path, filename_secure))
            item.image_url = f"uploads/{filename_secure}"

        db.session.commit()
        flash(f"{item_type.capitalize()} item updated successfully!", "success")
        return redirect(url_for(f"dashboard.{item_type}_items"))

    return render_template("add_edit_item.html", role=role, action="Edit", item=item, item_type=item_type)

# -----------------------------
# Delete Item
# -----------------------------
@dashboard_bp.route("/delete_item/<string:item_type>/<int:item_id>", methods=["POST"])
def delete_item(item_type, item_id):
    if item_type == "lost":
        item = LostItem.query.get_or_404(item_id)
    else:
        item = FoundItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash(f"{item_type.capitalize()} item deleted successfully!", "success")
    return redirect(url_for(f"dashboard.{item_type}_items"))
