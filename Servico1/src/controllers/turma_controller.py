from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session, joinedload
from ..config.base import SessionLocal
from ..models import Turma
from flasgger import swag_from
from ..docs.turma_docs import (
    list_turmas,
    get_turma,
    create_turma,
    update_turma,
    delete_turma
)

turma_bp = Blueprint("turma", __name__)

@turma_bp.route("/", methods=["GET"])
@swag_from(list_turmas)
def get_turmas():
    session: Session = SessionLocal()
    try:
        turmas = session.query(Turma).options(
            joinedload(Turma.alunos),
            joinedload(Turma.professor)
        ).all()
        result = formata_listagem(turmas)
        return result
    finally:
        session.close()

@turma_bp.route("/<int:id>", methods=["GET"])
@swag_from(get_turma)
def get_turma(id:int):
    session: Session = SessionLocal()
    turma = session.query(Turma).options(
        joinedload(Turma.alunos),
        joinedload(Turma.professor)
    ).get(id)
    session.close()
    
    if turma:
        return jsonify(formata_turma(turma))
    
    return jsonify({"error": "Turma não encontrada"}), 404

@turma_bp.route("/", methods=["POST"])
@swag_from(create_turma)
def create_turma():
    data = request.json
    
    session: Session = SessionLocal()
    
    turma = Turma(
        descricao=data["descricao"],
        professor_id=data["professor_id"]
    )
    
    session.add(turma)
    session.commit()
    session.refresh(turma)
    session.close()

    return jsonify({"id": turma.id, "message": "Turma criada com sucesso!"}), 201

@turma_bp.route("/<int:id>", methods=["PUT"])
@swag_from(update_turma)
def update_turma(id:int):
    data = request.json
    session: Session = SessionLocal()
    
    turma = session.query(Turma).get(id)
    if not turma:
        session.close()
        return jsonify({"error": "Turma não encontrada"}), 404
    
    turma.descricao = data.get("descricao", turma.descricao)
    turma.professor_id = data.get("professor_id", turma.professor_id)
    turma.ativo = data.get("ativo", turma.ativo)
    
    session.commit()
    session.refresh(turma)
    session.close()
    
    return jsonify({"id": turma.id, "message": "Turma atualizada com sucesso!"})

@turma_bp.route("/<int:id>", methods=["DELETE"])
@swag_from(delete_turma)
def delete_turma(id:int):
    session: Session = SessionLocal()
    
    turma = session.query(Turma).get(id)
    if not turma:
        session.close()
        return jsonify({"error": "Turma não encontrada"}), 404
    
    session.delete(turma)
    session.commit()
    session.close()
    
    return jsonify({"message": "Turma deletada com sucesso!"})

def formata_listagem(turmas:list[Turma]):
    turmas_formatadas = []
    for turma in turmas:
        turmas_formatadas.append(formata_turma(turma))

    return turmas_formatadas

def formata_turma(turma:Turma):
    alunos = []
    for aluno in turma.alunos:
        alunos.append({
            "id": aluno.id,
            "nome": aluno.nome,
            "idade": aluno.idade,
            "data_nascimento": aluno.data_nascimento.isoformat() if aluno.data_nascimento else None,
            "nota_primeiro_semestre": aluno.nota_primeiro_semestre,
            "nota_segundo_semestre": aluno.nota_segundo_semestre,
            "media_final": aluno.media_final
        })
    
    return {
        "id": turma.id,
        "descricao": turma.descricao,
        "professor": turma.professor.nome,
        "alunos": alunos
    }