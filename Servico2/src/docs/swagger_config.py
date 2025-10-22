from flasgger import Swagger

template = {
    "swagger": "2.0",
    "info": {
        "title": "API de Reservas",
        "description": "API para gerenciamento de reservas de salas",
        "version": "1.0.0"
    },
    "tags": [
        {
            "name": "Reservas",
            "description": "Operações relacionadas a reservas de salas"
        }
    ]
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/"
}

def setup_swagger(app):
    """Configura o Swagger com template personalizado"""
    swagger = Swagger(
        app,
        template=template,
        config=swagger_config
    )
    return swagger