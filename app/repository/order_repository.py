from app.entity import db
from app.repository.abstract_order_repository import AbstractOrderRepository
from app.entity.order import Order

class OrderRepository(AbstractOrderRepository):

    def create_order(self, data: dict) -> Order:
        new_order = Order(order_name=data['order_name'], order_code=data['order_code'])
        db.session.add(new_order)
        return new_order
