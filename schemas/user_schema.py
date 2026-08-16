from pydantic import BaseModel

class criarUsuario(BaseModel):
    usuario: str
    email: str
    telefone: str
    ativo: bool

class atualizarUsuario(BaseModel):
    usuario: str| None = None
    email: str| None = None
    telefone: str| None = None
    ativo: bool| None = None

class Usuario(BaseModel):
    id: int
    usuario: str
    email: str
    telefone: str
    ativo: bool