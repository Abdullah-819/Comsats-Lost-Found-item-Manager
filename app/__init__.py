from flask import Flask, redirect, url_for

def create_app():
    app = Flask(__name__)
    app.secret_key = "super_secret_key"

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

    return app
