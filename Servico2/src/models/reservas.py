from sqlalchemy import Boolean, Column, Date, Integer
from src.config.base import Base

class Reserva(Base):
    __tablename__ = 'reservas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    turma_id = Column(Integer, nullable=False)

    num_sala = Column(Integer, nullable=False)
    laboratorio = Column(Boolean, nullable=False, default=False)
    data = Column(Date, nullable=False)

    turma = []

    def to_dict(self):
        return {
            "id": self.id,
            "turma_id": self.turma_id,
            "turma": self.turma,
            "num_sala": self.num_sala,
            "laboratorio": self.laboratorio,
            "data": self.data.isoformat() if self.data else None
        }