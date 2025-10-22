"""
Documentação das rotas de professores.
"""

list_professors = {
    "summary": "Lista todos os professores",
    "tags": ["Professores"],
    "responses": {
        "200": {
            "description": "Lista de professores",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer",
                            "description": "ID do professor"
                        },
                        "nome": {
                            "type": "string",
                            "description": "Nome do professor"
                        },
                        "materia": {
                            "type": "string",
                            "description": "Matéria lecionada pelo professor"
                        },
                        "turmas": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "id": {
                                        "type": "integer",
                                        "description": "ID da turma"
                                    },
                                    "descricao": {
                                        "type": "string",
                                        "description": "Descrição da turma"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

get_professor = {
    "summary": "Retorna um professor específico",
    "tags": ["Professores"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID do professor"
        }
    ],
    "responses": {
        "200": {
            "description": "Dados do professor",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "ID do professor"
                    },
                    "nome": {
                        "type": "string",
                        "description": "Nome do professor"
                    },
                    "materia": {
                        "type": "string",
                        "description": "Matéria lecionada"
                    }
                }
            }
        },
        "404": {
            "description": "Professor não encontrado",
            "schema": {
                "type": "object",
                "properties": {
                    "error": {
                        "type": "string",
                        "description": "Mensagem de erro"
                    }
                }
            }
        }
    }
}

create_professor = {
    "summary": "Cria um novo professor",
    "tags": ["Professores"],
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "required": ["nome", "idade", "materia"],
                "properties": {
                    "nome": {
                        "type": "string",
                        "description": "Nome do professor"
                    },
                    "idade": {
                        "type": "integer",
                        "description": "Idade do professor"
                    },
                    "materia": {
                        "type": "string",
                        "description": "Matéria lecionada pelo professor"
                    },
                    "observacoes": {
                        "type": "string",
                        "description": "Observações adicionais"
                    }
                }
            }
        }
    ],
    "responses": {
        "201": {
            "description": "Professor criado com sucesso",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "ID do professor criado"
                    },
                    "message": {
                        "type": "string",
                        "description": "Mensagem de sucesso"
                    }
                }
            }
        }
    }
}

update_professor = {
    "summary": "Atualiza um professor existente",
    "tags": ["Professores"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID do professor"
        },
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "nome": {
                        "type": "string",
                        "description": "Nome do professor"
                    },
                    "idade": {
                        "type": "integer",
                        "description": "Idade do professor"
                    },
                    "materia": {
                        "type": "string",
                        "description": "Matéria lecionada pelo professor"
                    },
                    "observacoes": {
                        "type": "string",
                        "description": "Observações adicionais"
                    }
                }
            }
        }
    ],
    "responses": {
        "200": {
            "description": "Professor atualizado com sucesso",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "ID do professor"
                    },
                    "message": {
                        "type": "string",
                        "description": "Mensagem de sucesso"
                    }
                }
            }
        },
        "404": {
            "description": "Professor não encontrado",
            "schema": {
                "type": "object",
                "properties": {
                    "error": {
                        "type": "string",
                        "description": "Mensagem de erro"
                    }
                }
            }
        }
    }
}

delete_professor = {
    "summary": "Remove um professor",
    "tags": ["Professores"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID do professor"
        }
    ],
    "responses": {
        "200": {
            "description": "Professor removido com sucesso",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "Mensagem de sucesso"
                    }
                }
            }
        },
        "404": {
            "description": "Professor não encontrado",
            "schema": {
                "type": "object",
                "properties": {
                    "error": {
                        "type": "string",
                        "description": "Mensagem de erro"
                    }
                }
            }
        }
    }
}