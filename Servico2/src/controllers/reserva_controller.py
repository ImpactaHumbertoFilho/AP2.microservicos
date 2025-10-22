from flask import Blueprint, request
from sqlalchemy.orm import Session, joinedload
from datetime import datetime
from src.config.base import SessionLocal
from src.models.reservas import Reserva
from src.models.response import Response
from src.services.turma_service import TurmaService
from src.docs.reserva_docs import list_reservas, get_reserva, create_reserva
from flasgger import swag_from

reserva_bp = Blueprint("reserva", __name__) 

@reserva_bp.route("/", methods=["GET"])
@swag_from(list_reservas)
def get_reservas():
    session = SessionLocal()
    try:
        reservas = session.query(Reserva).all()

        if len(reservas) == 0 or reservas is None:
            return Response(status=204).to_response()

        return Response("Reservas encontradas", reservas).to_response()
    finally:
        session.close()

@reserva_bp.route("/<int:id>", methods=["GET"])
@swag_from(get_reserva)
def get_reserva(id):
    session = SessionLocal()
    try:
        reserva = session.query(Reserva).filter(Reserva.id == id).first()

        if reserva is None:
            return Response("Reserva não encontrada", status=404).to_response()

        turma_service = TurmaService()
        turma = turma_service.get_turma(reserva.turma_id)
        if not turma:
            return Response("Turma não encontrada no Serviço 1", status=404).to_response()

        reserva.turma = turma

        return Response("Reserva encontrada", reserva).to_response()
    finally:
        session.close()

@reserva_bp.route("/", methods=["POST"])
@swag_from(create_reserva)
def create_reserva():
    session = SessionLocal()
    try:
        data = request.get_json()
        if not data:
            return Response("Dados da reserva não fornecidos", status=400).to_response()

        required_fields = ['turma_id', 'num_sala', 'data']
        for field in required_fields:
            if field not in data:
                return Response(f"Campo {field} é obrigatório", status=400).to_response()

        turma_service = TurmaService()
        turma = turma_service.get_turma(data['turma_id'])
        if not turma:
            return Response("Turma não encontrada no Serviço 1", status=404).to_response()

        try:
            data_reserva = datetime.strptime(data['data'], '%Y-%m-%d').date()
        except ValueError:
            return Response("Formato de data inválido. Use YYYY-MM-DD", status=400).to_response()

        existing_reserva = session.query(Reserva).filter(
            Reserva.num_sala == data['num_sala'],
            Reserva.data == data_reserva
        ).first()

        if existing_reserva:
            return Response("Já existe uma reserva para esta sala nesta data", status=400).to_response()

        nova_reserva = Reserva(
            turma_id=data['turma_id'],
            num_sala=data['num_sala'],
            laboratorio=data.get('laboratorio', False),  # campo opcional
            data=data_reserva
        )

        session.add(nova_reserva)
        session.commit()

        return Response(
            "Reserva criada com sucesso",
            nova_reserva.to_dict(),
            201
        ).to_response()

    except Exception as e:
        session.rollback()
        return Response(f"Erro ao criar reserva: {str(e)}", status=500).to_response()
    finally:
        session.close()