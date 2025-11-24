from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Only one db instance for the whole app
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key = "super_secret_key"

    # Database config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cui_lf.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize db with this app
    db.init_app(app)

    # Import and register blueprints
    from app.routes.auth import auth_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.role_selection import role_bp
    from app.routes.home import home_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(role_bp)
    app.register_blueprint(home_bp)

    @app.route("/")
    def index():
        return redirect(url_for("role.select_role"))

    return app
