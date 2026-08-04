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
#    URL\users\{id} (GET),
#    URL\users\{id} (PUT)
#    URL\users\{id} (POST),
#    URL\users\{id} (DELETE)
# }
#Recursos disponibilizados: Informações sobre os usuários

app = FastAPI()

#GET, sem parametro, exibe todos os usuarios
@app.get('/users')
def get_user():
    return users.listar_usuarios()

#GET, por ID, exibe apenas o usuario do ID informado
@app.get('/users/{id}')
def get_user_por_id(id: int):
    return users.listar_usuarios_id(id)

#PUT, por ID, atualiza os dados de um usuario especifico
@app.put('/users/{id}')
def put_atualizar_user (id: int, usuario: Usuario):
    return users.atualizar_usuario(id, usuario.model_dump())

#POST, sem parametro, cadastra um usuario novo
@app.post('/users')
def post_novo_user(usuario: Usuario):
    return users.criar_usuario(usuario.model_dump())