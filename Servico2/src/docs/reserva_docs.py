"""
Documentação das rotas de reservas.
"""

list_reservas = {
    "summary": "Lista todas as reservas",
    "tags": ["Reservas"],
    "responses": {
        "200": {
            "description": "Lista de reservas encontradas",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "example": "Reservas encontradas"
                    },
                    "data": {
                        "type": "object",
                        "properties": {
                            "reservas": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer",
                                            "description": "ID da reserva"
                                        },
                                        "turma_id": {
                                            "type": "integer",
                                            "description": "ID da turma"
                                        },
                                        "num_sala": {
                                            "type": "integer",
                                            "description": "Número da sala"
                                        },
                                        "laboratorio": {
                                            "type": "boolean",
                                            "description": "Indica se é um laboratório"
                                        },
                                        "data": {
                                            "type": "string",
                                            "format": "date",
                                            "description": "Data da reserva"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "204": {
            "description": "Nenhuma reserva encontrada"
        }
    }
}

get_reserva = {
    "summary": "Obtém uma reserva por ID",
    "tags": ["Reservas"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID da reserva"
        }
    ],
    "responses": {
        "200": {
            "description": "Detalhes da reserva",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "example": "Reserva encontrada"
                    },
                    "data": {
                        "type": "object",
                        "properties": {
                            "reserva": {
                                "type": "object",
                                "properties": {
                                    "id": {
                                        "type": "integer",
                                        "description": "ID da reserva"
                                    },
                                    "turma_id": {
                                        "type": "integer",
                                        "description": "ID da turma"
                                    },
                                    "num_sala": {
                                        "type": "integer",
                                        "description": "Número da sala"
                                    },
                                    "laboratorio": {
                                        "type": "boolean",
                                        "description": "Indica se é um laboratório"
                                    },
                                    "data": {
                                        "type": "string",
                                        "format": "date",
                                        "description": "Data da reserva"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "404": {
            "description": "Reserva não encontrada"
        }
    }
}

create_reserva = {
    "summary": "Cria uma nova reserva",
    "tags": ["Reservas"],
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "turma_id": {
                        "type": "integer",
                        "description": "ID da turma que será vinculada à reserva"
                    },
                    "num_sala": {
                        "type": "integer",
                        "description": "Número da sala"
                    },
                    "laboratorio": {
                        "type": "boolean",
                        "description": "Indica se é um laboratório",
                        "default": False
                    },
                    "data": {
                        "type": "string",
                        "format": "date",
                        "description": "Data da reserva (formato: YYYY-MM-DD)"
                    }
                },
                "required": ["turma_id", "num_sala", "data"]
            }
        }
    ],
    "responses": {
        "201": {
            "description": "Reserva criada com sucesso",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "example": "Reserva criada com sucesso"
                    },
                    "data": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "integer",
                                "description": "ID da reserva criada"
                            }
                        }
                    }
                }
            }
        },
        "400": {
            "description": "Erro ao criar reserva",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "Mensagem de erro"
                    }
                }
            }
        }
    }
}