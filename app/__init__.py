from flask import Flask
from app.config import Config
from app.routes import init_routes
from app.entity import db

def create_app():
    app = Flask(__name__)
    # Add config application
    app.config.from_object(Config)
    # Add config database
    db.init_app(app)

    with app.app_context():
        db.create_all()  # Tạo bảng database nếu chưa tồn tại

    # Management session in request context
    @app.before_request
    def before_request():
        # Open new session
        db.session()

    @app.teardown_request
    def teardown_request(exception=None):
        # Handle session: Commit or rollback when request end
        if exception:
            db.session.rollback()
        else:
            try:
                db.session.commit()
            except:
                db.session.rollback()
                raise
            finally:
                db.session.remove()

    # Add config routes
    init_routes(app)
    return app
