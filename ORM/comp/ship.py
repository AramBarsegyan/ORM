from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from comp.base import Base

class Ship(Base):
    __tablename__ = 'ship'

    id = Column(Integer, primary_key=True, index=True)
    ship_name = Column(String, index=True)

    # Связь с моделью Voyage
    voyages = relationship("Voyage", back_populates="ship")

    def __init__(self, ship_name: str):
        self.ship_name = ship_name
