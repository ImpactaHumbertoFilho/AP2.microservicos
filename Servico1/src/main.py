from .config.base import Base, engine
from .models import Professor, Turma, Aluno
from flask import Flask
from .docs.swagger_config import setup_swagger
from flasgger import Swagger

from .controllers.professor_controller import professor_bp
from .controllers.aluno_controller import aluno_bp
from .controllers.turma_controller import turma_bp

def create_app():
    app = Flask(__name__)

    # Config do banco (exemplo com SQLite, pode trocar por PostgreSQL/MySQL)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///meu_banco.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # Cria as tabelas
    Base.metadata.create_all(bind=engine)

    # Configura o Swagger
    setup_swagger(app)

    # Importa e registra os blueprints (controllers)
    app.register_blueprint(professor_bp, url_prefix="/professores")
    app.register_blueprint(aluno_bp, url_prefix="/alunos")
    app.register_blueprint(turma_bp, url_prefix="/turmas")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)