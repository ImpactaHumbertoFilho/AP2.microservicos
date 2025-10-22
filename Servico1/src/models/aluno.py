from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..config.base import Base


class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    idade = Column(Integer, nullable=False)
    turma_id = Column(Integer, ForeignKey("turmas.id"), nullable=False)
    data_nascimento = Column(Date, nullable=True)
    nota_primeiro_semestre = Column(Float, nullable=True)
    nota_segundo_semestre = Column(Float, nullable=True)
    media_final = Column(Float, nullable=True)

    turma = relationship("Turma", back_populates="alunos")
