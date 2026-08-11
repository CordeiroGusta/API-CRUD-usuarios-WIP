from fastapi import FastAPI
from pydantic import BaseModel
import users

class Usuario(BaseModel):
    id: int
    usuario: str
    email: str
    telefone: str
    ativo: bool

app = FastAPI()

@app.get('/users')
def get_user():
    return users.listar_usuarios()

@app.get('/users/{id}')
def get_user_por_id(id: int):
    return users.listar_usuarios_id(id)

@app.put('/users/{id}')
def put_atualizar_user (id: int, usuario: Usuario):
    return users.atualizar_usuario(id, usuario.model_dump())

@app.post('/users')
def post_novo_user(usuario: Usuario):
    return users.criar_usuario(usuario.model_dump())

@app.delete('/users/{id}')
def delete_apagar_user(id: int):
    return users.deletar_usuario(id)