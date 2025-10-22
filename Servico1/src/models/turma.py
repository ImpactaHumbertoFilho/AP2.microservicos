from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..config.base import Base


class Turma(Base):
    __tablename__ = "turmas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(100), nullable=False)
    professor_id = Column(Integer, ForeignKey("professores.id"), nullable=False)
    ativo = Column(Boolean, default=True)

    professor = relationship("Professor", back_populates="turmas")
    alunos = relationship("Aluno", back_populates="turma", cascade="all, delete-orphan")
