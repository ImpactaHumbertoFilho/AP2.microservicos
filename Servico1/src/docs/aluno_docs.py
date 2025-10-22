"""
Documentação das rotas de alunos.
"""

list_alunos = {
    "summary": "Lista todos os alunos",
    "tags": ["Alunos"],
    "responses": {
        "200": {
            "description": "Lista de alunos",
            "schema": {
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
                        "turma": {
                            "type": "string",
                            "description": "Descrição da turma do aluno"
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

get_aluno = {
    "summary": "Obtém um aluno por ID",
    "tags": ["Alunos"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID do aluno"
        }
    ],
    "responses": {
        "200": {
            "description": "Detalhes do aluno",
            "schema": {
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
                    "turma": {
                        "type": "string",
                        "description": "Descrição da turma do aluno"
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
        },
        "404": {
            "description": "Aluno não encontrado"
        }
    }
}

create_aluno = {
    "summary": "Cria um novo aluno",
    "tags": ["Alunos"],
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "nome": {
                        "type": "string",
                        "description": "Nome do aluno"
                    },
                    "idade": {
                        "type": "integer",
                        "description": "Idade do aluno"
                    },
                    "turma_id": {
                        "type": "integer",
                        "description": "ID da turma do aluno"
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
                },
                "required": ["nome", "idade", "turma_id"]
            }
        }
    ],
    "responses": {
        "201": {
            "description": "Aluno criado com sucesso",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "example": "Aluno criado com sucesso"
                    },
                    "id": {
                        "type": "integer",
                        "description": "ID do aluno criado"
                    }
                }
            }
        },
        "400": {
            "description": "Erro ao criar aluno",
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

update_aluno = {
    "summary": "Atualiza um aluno existente",
    "tags": ["Alunos"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID do aluno"
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
                        "description": "Nome do aluno"
                    },
                    "idade": {
                        "type": "integer",
                        "description": "Idade do aluno"
                    },
                    "turma_id": {
                        "type": "integer",
                        "description": "ID da turma do aluno"
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
    ],
    "responses": {
        "200": {
            "description": "Aluno atualizado com sucesso"
        },
        "404": {
            "description": "Aluno não encontrado"
        }
    }
}

delete_aluno = {
    "summary": "Deleta um aluno por ID",
    "tags": ["Alunos"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID do aluno"
        }
    ],
    "responses": {
        "200": {
            "description": "Aluno deletado com sucesso"
        },
        "404": {
            "description": "Aluno não encontrado"
        }
    }
}