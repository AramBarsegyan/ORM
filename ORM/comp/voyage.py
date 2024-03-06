from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from comp.base import Base

class Voyage(Base):
    __tablename__ = 'voyage'

    id = Column(Integer, primary_key=True, index=True)
    voyage_number = Column(String, index=True)
    destination = Column(String)
    ship_id = Column(Integer, ForeignKey('ship.id'))

    # Связь обратно к модели Ship
    ship = relationship("Ship", back_populates="voyages")

    def __init__(self, voyage_number: str, destination: str, ship_id: int):
        self.voyage_number = voyage_number
        self.destination = destination
        self.ship_id = ship_id
