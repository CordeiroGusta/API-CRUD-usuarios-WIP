from fastapi import FastAPI
import users

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

#GET geral
@app.get('/users')
def get_user():
    return users.listar_usuarios()

@app.get('/users/{id}')
def get_user_por_id(id: int):
    return users.listar_usuarios_id(id)

@app.post('/users')
