from flask import Flask, redirect, url_for

def create_app():
    app = Flask(__name__)
    app.secret_key = "super_secret_key"  # needed for session & flash

    # Import blueprints
    from app.routes.auth import auth_bp
    from app.routes.dashboard import dashboard_bp

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)

    # Redirect root '/' to login page
    @app.route("/")
    def index():
        return redirect(url_for("auth.login"))

    return app
