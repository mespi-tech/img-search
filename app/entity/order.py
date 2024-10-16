from . import db

class Order(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    order_name      = db.Column(db.String(120), nullable=False)
    order_code      = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.order_name}>'

    def json(self):
        return {"id": self.id, "order_name": self.order_name, "order_code": self.order_code}
