
from flask import Flask
from Servico2.src.config.base import Base, engine
from Servico2.src.models.response import Response
from Servico2.src.controllers.reserva_controller import reserva_bp
from Servico2.src.docs.swagger_config import setup_swagger

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco_servico-2.db"
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