from flask import jsonify
from typing import Any, Dict, List, Union

class Response:
    def __init__(self, message: str = "", data: Union[Dict, List, Any] = None, status: int = 200):
        self.message = message
        self.data = data if data is not None else {}
        self.status = status

    def _get_object_name(self, obj: Any) -> str:
        if isinstance(obj, dict):
            # Se já é um dicionário, retorna a primeira chave ou 'data'
            return next(iter(obj.keys())) if obj else 'data'
        
        if isinstance(obj, list):
            # Se for uma lista vazia, retorna 'items'
            if not obj:
                return 'items'
            # Para lista, pega o nome do primeiro item e pluraliza
            name = obj[0].__class__.__name__.lower()
            return f"{name}s"
        
        # Para objeto único, retorna o nome da classe em lowercase
        return obj.__class__.__name__.lower()

    def _convert_data(self, data: Any) -> Any:
        if hasattr(data, 'to_dict'):
            return data.to_dict()
        elif isinstance(data, list):
            return [self._convert_data(item) for item in data]
        
        return data

    def to_response(self):
        converted_data = self._convert_data(self.data)
        # Se data já é um dicionário, mantém como está
        if isinstance(self.data, dict):
            response_data = converted_data
        else:
            # Caso contrário, cria um dicionário com o nome apropriado
            key = self._get_object_name(self.data)
            response_data = {key: converted_data}

        return jsonify({
            "message": self.message,
            **response_data
        }), self.status