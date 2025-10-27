# AP2.microservicos

Repositório de exemplo com arquitetura de microserviços para a AP2.
Este repositório contém atualmente dois microserviços prontos: `Servico1` (API Escola) e `Servico2` (API Reservas) e `Servico3` (API Atividades).

## Visão geral

- Servico1: API para gerenciamento de professores, alunos e turmas.
  - Porta: 5000
  - Tecnologias: Flask, SQLAlchemy, Flasgger (Swagger)

- Servico2: API para gerenciamento de reservas de salas.
  - Porta: 5001
  - Tecnologias: Flask, SQLAlchemy, Flasgger (Swagger), Requests (consome Servico1)
- Servico3: API para gerenciamento de Atividades e notas.
  - Porta: 5002
  - Tecnologias: Flask, SQLAlchemy, Flasgger (Swagger), Requests (consome Servico1)

Todos os serviços usam SQLite como banco local dentro do container e estão preparados para rodar via Docker/Docker Compose.

---

## Pré-requisitos

- Docker
- Docker Compose (ou o plugin `docker compose` moderno)
- PowerShell (os comandos abaixo usam PowerShell como shell)

---

## Como construir as imagens

Para construir todas as imagens definidas no `docker-compose.yml` (recomendado):

```powershell
cd 
docker compose build
```

Para construir apenas um serviço (ex.: Servico1):

```powershell
cd \Servico1
docker build -t servico1:latest .
```

```powershell
cd \Servico2
docker build -t servico2:latest .
```

```powershell
cd \Servico3
docker build -t servico3:latest .
```
---

## Como executar (Docker Compose)

Para subir todos os serviços (construir e executar):

```powershell
docker-compose up --build
```

Observações:
- O `docker-compose.yml` na raiz já está preparado para orquestrar `Servico1` e `Servico2` numa rede `microservices-network`.
- `Servico2` depende de `Servico1` (configuração `depends_on` baseada em healthcheck) para garantir que as requisições entre serviços funcionem.

Para rodar em background (detached):

```powershell
docker-compose up --build -d
```

Para parar e remover containers e rede criada pelo compose:

```powershell
docker-compose down
```

---

## Endpoints principais (teste rápido)

- Servico1 (API Escola)
  - Swagger UI: http://localhost:5000/swagger/
  - Professores: http://localhost:5000/professores
  - Alunos: http://localhost:5000/alunos
  - Turmas: http://localhost:5000/turmas

- Servico2 (API Reservas)
  - Swagger UI: http://localhost:5001/swagger/
  - Reservas: http://localhost:5001/reservas

- Servico2 (API Atividades)
  - Swagger UI: http://localhost:5002/swagger/
  - Reservas: http://localhost:5002/atividades

Use o Swagger UI de cada serviço para ver a documentação das rotas e testar as APIs.

---

## Observações sobre arquitetura e comunicação

- Comunicação entre serviços: feita via requests HTTP. Dentro do Docker, cada serviço usa o nome do serviço como hostname (ex.: `http://servico1:5000`) para se comunicar.
- Healthchecks: o `servico1` possui um healthcheck que verifica `/swagger/` usando `curl` (por isso a imagem do Servico1 instala `curl`). O `servico2` possui um healthcheck que tenta acessar seu próprio `/swagger/`.
- Persistência: os bancos são arquivos SQLite localizados dentro de cada container (ex.: `banco_servico1.db`, `banco_servico2.db`, `banco_servico3.db`). Para persistência real entre reinícios, adicione volumes no `docker-compose.yml`.

---

## Dicas e troubleshooting

- Se um serviço não iniciar, verifique os logs com:

```powershell
docker-compose logs -f servico1
# ou
docker-compose logs -f servico2
# ou
docker-compose logs -f servico3
```

- Se o `docker-compose` reclamar sobre a chave `version` no topo do arquivo, pode ignorar por enquanto — algumas versões atuais do compose mostram um aviso. Você pode remover a linha `version: '3.8'` para silenciar o aviso.

- Para depurar chamadas entre serviços, entre no container e use curl:

```powershell
docker exec -it servico2 powershell
# Dentro do container (Linux shell), usar curl:
curl http://servico1:5000/swagger/
```

---