from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = "super_secret_key"  # needed for session & flash

    # Register blueprints
    from app.routes.home import home_bp
    app.register_blueprint(home_bp)

    return app
