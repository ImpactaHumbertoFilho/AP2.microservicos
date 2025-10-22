
from flask import Flask
from src.config.base import Base, engine
from src.models.response import Response
from src.controllers.reserva_controller import reserva_bp
from src.docs.swagger_config import setup_swagger

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco_servico2.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # Cria as tabelas
    #Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Configura o Swagger
    setup_swagger(app)

    # Importa e registra os blueprints (controllers)
    app.register_blueprint(reserva_bp, url_prefix="/reservas")
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host= '0.0.0.0', port=5001, debug=True)