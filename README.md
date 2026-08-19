# 🚀 API CRUD de Usuários

API REST desenvolvida com **Python e FastAPI** como projeto de estudo e evolução prática em desenvolvimento de APIs.

## 📌 Sobre o projeto

A aplicação implementa uma API para gerenciamento de usuários. Nesta etapa, os dados são mantidos **em memória**, utilizando uma lista de dicionários.

```python
usuarios = [
    {
        "id": 1,
        "usuario": "Gustavo",
        "email": "gustavo@email.com",
        "telefone": "11999999999",
        "ativo": True
    }
]
```

Essa abordagem é intencional: primeiro são trabalhados HTTP, CRUD, validação, arquitetura e regras de negócio; posteriormente a persistência será migrada para PostgreSQL.

> **Status:** Em desenvolvimento / Projeto de estudo

---

# 🛠️ Tecnologias

### Atualmente

- Python
- FastAPI
- Pydantic
- Uvicorn

### Planejado

- PostgreSQL
- SQLAlchemy
- Alembic
- Pytest
- Docker / Docker Compose
- JWT
- Autenticação e autorização
- Boas práticas de segurança

---

# 📁 Estrutura do projeto

```text
app/
├── main.py
├── routers/
│   └── users.py
├── schemas/
│   └── user.py
├── services/
│   └── user_service.py
├── repositories/
│   └── user_repository.py
├── database/
│   ├── connection.py
│   └── models.py
└── core/
    ├── security.py
    └── config.py

tests/
└── ...
```

Algumas dessas camadas ainda estão em desenvolvimento e serão implementadas progressivamente.

---

# 🧠 Arquitetura

A arquitetura planejada segue uma separação de responsabilidades:

```text
Cliente
   │
   ▼
Router
   │
   ▼
Schema
   │
   ▼
Service
   │
   ▼
Repository
   │
   ▼
Database
```

### Router

Responsável pela camada HTTP e pelo direcionamento das requisições.

```text
GET    /api/v1/users
GET    /api/v1/users/{id}
POST   /api/v1/users
PUT  /api/v1/users/{id}
DELETE /api/v1/users/{id}
```

### Schema

Define o formato dos dados que entram e saem da API.

```python
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    usuario: str
    email: EmailStr
    telefone: str
    ativo: bool
```

O Schema funciona como um **contrato da API**, validando a estrutura dos dados.

### Service

Responsável pelas **regras de negócio**, como verificar se um usuário pode ser criado ou se um email já está cadastrado.

### Repository

Responsável pelo acesso aos dados. Atualmente utiliza a lista em memória; futuramente será a camada de comunicação com o PostgreSQL.

### Database

Responsável pela persistência.

Atual:

```text
Aplicação
   ↓
Lista Python
```

Planejado:

```text
Aplicação
   ↓
SQLAlchemy
   ↓
PostgreSQL
```

### Core

Concentrará configurações, variáveis de ambiente, segurança, autenticação e componentes compartilhados da aplicação.

---

# 🔄 CRUD

| Operação | HTTP | Endpoint |
|---|---|---|
| Listar usuários | GET | `/api/v1/users` |
| Buscar usuário | GET | `/api/v1/users/{id}` |
| Criar usuário | POST | `/api/v1/users` |
| Atualizar usuário | PUT | `/api/v1/users/{id}` |
| Excluir usuário | DELETE | `/api/v1/users/{id}` |

---

# 📡 Exemplos

## Listar usuários

```http
GET /api/v1/users
```

Exemplo de resposta:

```json
[
    {
        "id": 1,
        "usuario": "Gustavo",
        "email": "gustavo@email.com",
        "telefone": "11999999999",
        "ativo": true
    }
]
```

## Buscar usuário

```http
GET /api/v1/users/1
```

## Criar usuário

```http
POST /api/v1/users
```

Body:

```json
{
    "usuario": "Gustavo",
    "email": "gustavo@email.com",
    "telefone": "11999999999",
    "ativo": true
}
```

O ID deverá ser responsabilidade da aplicação, e não do cliente.

## Atualizar usuário

```http
PUT /api/v1/users/1
```

Body:

```json
{
    "email": "novo@email.com"
}
```

## Excluir usuário

```http
DELETE /api/v1/users/1
```

Quando realizada corretamente:

```http
204 No Content
```

---

# ⚠️ Tratamento de erros

| Situação | Status |
|---|---:|
| Requisição realizada com sucesso | `200 OK` |
| Usuário criado | `201 Created` |
| Recurso excluído | `204 No Content` |
| Usuário não encontrado | `404 Not Found` |
| Recurso já existente/conflito | `409 Conflict` |
| Dados inválidos | `422 Unprocessable Entity` |

Exemplo:

```python
from fastapi import HTTPException

if usuario is None:
    raise HTTPException(
        status_code=404,
        detail="Usuário não encontrado"
    )
```

---

# ▶️ Como executar

## 1. Clonar o projeto

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_PROJETO>
```

## 2. Criar ambiente virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Instalar dependências

```bash
pip install -r requirements.txt
```

## 4. Executar

```bash
uvicorn app.main:app --reload
```

---

# 📖 Documentação automática

FastAPI fornece documentação interativa automaticamente.

### Swagger

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

O Swagger permite testar os endpoints diretamente pelo navegador.

---

# 🧪 Testes

A próxima etapa é implementar testes automatizados utilizando **Pytest**.

Os testes deverão verificar cenários de sucesso e de erro.

```text
Criar usuário
    ├── dados válidos → 201
    ├── email inválido → erro de validação
    └── email duplicado → 409

Buscar usuário
    ├── usuário existente → 200
    └── usuário inexistente → 404

Excluir usuário
    ├── usuário existente → 204
    └── usuário inexistente → 404
```

A intenção é transformar os comportamentos esperados da API em verificações automatizadas.

---

# 🗺️ Roadmap

## 🟢 Etapa 1 — CRUD em memória

- [x] Criar API com FastAPI
- [x] Criar endpoints de usuários
- [x] Listar usuários
- [x] Buscar usuário por ID
- [x] Criar usuário
- [x] Atualizar usuário
- [x] Excluir usuário
- [x] Utilizar Pydantic
- [x] Utilizar códigos HTTP
- [x] Tratamento inicial de erros

## 🟡 Etapa 2 — Organização

- [ ] Separar routers
- [ ] Criar schemas de entrada e saída
- [ ] Criar services
- [ ] Criar repositories
- [ ] Implementar geração automática de IDs
- [ ] Melhorar validações
- [ ] Implementar validação de email duplicado
- [ ] Padronizar respostas HTTP

## 🟠 Etapa 3 — Testes

- [ ] Configurar Pytest
- [ ] Testar endpoints
- [ ] Testar regras de negócio
- [ ] Testar casos de erro
- [ ] Criar testes de integração

## 🔵 Etapa 4 — Banco de dados

- [ ] PostgreSQL
- [ ] SQLAlchemy
- [ ] Models
- [ ] Connection/Session
- [ ] Migrations com Alembic
- [ ] Constraints e índices

## 🟣 Etapa 5 — Infraestrutura

- [ ] Docker
- [ ] Docker Compose
- [ ] Container da API
- [ ] Container do PostgreSQL
- [ ] Variáveis de ambiente

## 🔴 Etapa 6 — Segurança

- [ ] Hash de senhas
- [ ] Login
- [ ] JWT
- [ ] Refresh tokens
- [ ] Autenticação
- [ ] Autorização
- [ ] CORS
- [ ] Rate limiting
- [ ] Gerenciamento de secrets

---

# 🎯 Objetivo do projeto

Mais do que construir um CRUD de usuários, este projeto serve como laboratório para compreender o funcionamento de uma API moderna.

A evolução planejada segue:

```text
Python
   ↓
FastAPI
   ↓
HTTP / REST
   ↓
Pydantic
   ↓
Arquitetura em camadas
   ↓
Testes
   ↓
PostgreSQL
   ↓
SQLAlchemy
   ↓
Docker
   ↓
Autenticação
   ↓
Segurança
```

A implementação será incremental, priorizando a compreensão dos conceitos antes da introdução de novas ferramentas.

---

# 📚 Conceitos estudados

- APIs REST
- HTTP
- CRUD
- FastAPI
- Pydantic
- validação de dados
- schemas
- routers
- services
- repositories
- persistência
- códigos de status
- tratamento de exceções
- testes automatizados
- bancos relacionais
- ORM
- Docker
- autenticação
- autorização
- segurança de APIs

---

## 🚧 Projeto em desenvolvimento

Este projeto está sendo desenvolvido incrementalmente como parte do processo de aprendizado em desenvolvimento backend.

Novas funcionalidades e melhorias serão implementadas conforme os conceitos forem estudados e consolidados.
