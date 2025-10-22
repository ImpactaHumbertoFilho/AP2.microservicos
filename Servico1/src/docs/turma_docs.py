"""
Documentação das rotas de turmas.
"""

list_turmas = {
    "summary": "Lista todas as turmas",
    "tags": ["Turmas"],
    "responses": {
        "200": {
            "description": "Lista de turmas",
            "schema": {
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
                        },
                        "professor": {
                            "type": "string",
                            "description": "Nome do professor"
                        },
                        "alunos": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "id": {
                                        "type": "integer",
                                        "description": "ID do aluno"
                                    },
                                    "nome": {
                                        "type": "string",
                                        "description": "Nome do aluno"
                                    },
                                    "idade": {
                                        "type": "integer",
                                        "description": "Idade do aluno"
                                    },
                                    "data_nascimento": {
                                        "type": "string",
                                        "format": "date",
                                        "description": "Data de nascimento do aluno"
                                    },
                                    "nota_primeiro_semestre": {
                                        "type": "number",
                                        "description": "Nota do primeiro semestre"
                                    },
                                    "nota_segundo_semestre": {
                                        "type": "number",
                                        "description": "Nota do segundo semestre"
                                    },
                                    "media_final": {
                                        "type": "number",
                                        "description": "Média final do aluno"
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

get_turma = {
    "summary": "Retorna uma turma específica",
    "tags": ["Turmas"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID da turma"
        }
    ],
    "responses": {
        "200": {
            "description": "Dados da turma",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "ID da turma"
                    },
                    "descricao": {
                        "type": "string",
                        "description": "Descrição da turma"
                    },
                    "professor": {
                        "type": "string",
                        "description": "Nome do professor"
                    },
                    "alunos": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer",
                                    "description": "ID do aluno"
                                },
                                "nome": {
                                    "type": "string",
                                    "description": "Nome do aluno"
                                },
                                "idade": {
                                    "type": "integer",
                                    "description": "Idade do aluno"
                                },
                                "data_nascimento": {
                                    "type": "string",
                                    "format": "date",
                                    "description": "Data de nascimento do aluno"
                                },
                                "nota_primeiro_semestre": {
                                    "type": "number",
                                    "description": "Nota do primeiro semestre"
                                },
                                "nota_segundo_semestre": {
                                    "type": "number",
                                    "description": "Nota do segundo semestre"
                                },
                                "media_final": {
                                    "type": "number",
                                    "description": "Média final do aluno"
                                }
                            }
                        }
                    }
                }
            }
        },
        "404": {
            "description": "Turma não encontrada",
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

create_turma = {
    "summary": "Cria uma nova turma",
    "tags": ["Turmas"],
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "required": ["descricao", "professor_id"],
                "properties": {
                    "descricao": {
                        "type": "string",
                        "description": "Descrição da turma"
                    },
                    "professor_id": {
                        "type": "integer",
                        "description": "ID do professor responsável"
                    }
                }
            }
        }
    ],
    "responses": {
        "201": {
            "description": "Turma criada com sucesso",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "ID da turma criada"
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

update_turma = {
    "summary": "Atualiza uma turma existente",
    "tags": ["Turmas"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID da turma"
        },
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "descricao": {
                        "type": "string",
                        "description": "Nova descrição da turma"
                    },
                    "professor_id": {
                        "type": "integer",
                        "description": "Novo ID do professor responsável"
                    },
                    "ativo": {
                        "type": "boolean",
                        "description": "Status de ativação da turma"
                    }
                }
            }
        }
    ],
    "responses": {
        "200": {
            "description": "Turma atualizada com sucesso",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "ID da turma"
                    },
                    "message": {
                        "type": "string",
                        "description": "Mensagem de sucesso"
                    }
                }
            }
        },
        "404": {
            "description": "Turma não encontrada",
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

delete_turma = {
    "summary": "Remove uma turma",
    "tags": ["Turmas"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID da turma"
        }
    ],
    "responses": {
        "200": {
            "description": "Turma removida com sucesso",
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
            "description": "Turma não encontrada",
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