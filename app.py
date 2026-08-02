from fastapi import FastAPI

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


