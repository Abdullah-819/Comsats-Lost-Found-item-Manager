from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy (OOP models will use this)
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key = "super_secret_key"

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lost_found.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database with app
    db.init_app(app)

    # Import blueprints
    from app.routes.auth import auth_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.role_selection import role_bp
    from app.routes.home import home_bp

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(role_bp)
    app.register_blueprint(home_bp)

    # Redirect root '/' to role selection page
    @app.route("/")
    def index():
        return redirect(url_for("role.select_role"))

    # Create all tables if they don't exist
    with app.app_context():
        from app.model.models import User, LostItem, FoundItem  # Import models
        db.create_all()

    return app
