from fastapi import FastAPI
from pydantic import BaseModel
import users

class Usuario(BaseModel):
    id: int
    usuario: str
    email: str
    telefone: str
    ativo: bool

#Objetivo: Crud de usuários
#Url: vai ser gerada pelo Uvicorn
#Endpoints: {
#    URL\users (GET),
#    URL\user\{id} (GET),
#    URL\users\{id} (POST),
#    URL\users\{id} (DELETE)
# }
#Recursos disponibilizados: Informações sobre os usuários

app = FastAPI()

#GET geral, exibe todos os usuarios
@app.get('/users')
def get_user():
    return users.listar_usuarios()

#GET por ID, exibe apenas o usuario do ID informado
@app.get('/users/{id}')
def get_user_por_id(id: int):
    return users.listar_usuarios_id(id)

#PUT por ID, atualiza os dados de um usuario especifico
@app.put('/users/{id}')
def put_atualizar_user (id: int, usuario: Usuario):
    return users.atualizar_usuario(id, usuario.model_dump())