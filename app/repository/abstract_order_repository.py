from abc import ABC, abstractmethod
from typing import List
from app.entity.order import Order

class AbstractOrderRepository(ABC):

    @abstractmethod
    def create_order(self, data: dict) -> Order:
        pass
