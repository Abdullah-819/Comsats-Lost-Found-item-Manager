from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "your-secret-key"

    # -----------------------
    # Import & register routes
    # -----------------------
    from app.routes.auth import auth_bp
    from app.routes.dashboard import dashboard_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)

    return app
