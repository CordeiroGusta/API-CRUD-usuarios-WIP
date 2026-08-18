from fastapi import FastAPI,HTTPException
from schemas.user_schema import criarUsuario, atualizarUsuario, Usuario
import users

app = FastAPI()

@app.get('/api/v1/users')
def get_user():
    usuarios = users.listar_usuarios()
    return usuarios

@app.get('/api/v1/users/{id}')
def get_user_por_id(id: int):
    usuario = users.listar_usuarios_id(id)
    if usuario == None:
        raise HTTPException(
            status_code=404,
            detail= {
                "status": 404,
                "code": "USER_NOT_FOUND",
                "message": "Usuario não encontrado  " 
            }
        )
    return usuario

@app.put('/api/v1/users/{id}')
def put_atualizar_user (id: int, usuario: atualizarUsuario):
    dados = usuario.model_dump(exclude_unset=True)
    usuario_atualizado = users.atualizar_usuario(id, dados)
    return usuario_atualizado

@app.post('/api/v1/users')
def post_novo_user(usuario: Usuario):
    novo_usuario = users.criar_usuario(usuario.model_dump()) 
    return novo_usuario

@app.delete('/api/v1/users/{id}')
def delete_apagar_user(id: int):
    usuario_deletado = users.deletar_usuario(id)
    return usuario_deletado