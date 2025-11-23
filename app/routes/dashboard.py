from flask import Blueprint, render_template, session

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

# Main dashboard
@dashboard_bp.route("/")
def dashboard_view():
    role = session.get("role", "user")  # default = user

    stats = {
        "items_lost": 5,
        "items_found": 3,
        "resolved": 2
    }

    return render_template("dashboard.html", role=role, stats=stats)

# LOST ITEMS PAGE
@dashboard_bp.route("/lost")
def lost_items():
    from app.manager.item_manager import get_lost_items
    items = get_lost_items()
    role = session.get("role", "user")
    return render_template("lost_items.html", items=items, role=role)

# FOUND ITEMS PAGE
@dashboard_bp.route("/found")
def found_items():
    from app.manager.item_manager import get_found_items
    items = get_found_items()
    role = session.get("role", "user")
    return render_template("found_items.html", items=items, role=role)
