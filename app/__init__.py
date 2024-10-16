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
    # Add config routes
    init_routes(app)
    return app
