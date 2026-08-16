usuarios = [
    {
        "id": 1,
        "usuario": "fulano",
        "email": "fulanonice@sememail.com",
        "telefone": "4112345678",
        "ativo": True
    },
    {
        "id": 2,
        "usuario": "ciclano",
        "email": "bacana@sememail.com",
        "telefone": "4187654321",
        "ativo": True
    },
    {
        "id": 3,
        "usuario": "billy",
        "email": "dev@sememail.com",
        "telefone": "4111223344",
        "ativo": True
    },
    {
        "id": 4,
        "usuario": "roberts",
        "email": "dataengineer@sememail.com",
        "telefone": "4188776655",
        "ativo": False
    }
]

#metodos
def listar_usuarios():
    '''Lista todos os usuários da base de dados'''
    return usuarios

def listar_usuarios_id(id):
    '''Lista o usuario que corresponder ao id fornecido'''
    for usuario in usuarios:
        if usuario['id'] == id:
            return usuario

def atualizar_usuario(id, usuario_atualizado):
    '''Atualiza os dados de um usuario que corresponder ao id fornecido'''
    for indice, usuario in enumerate(usuarios):
        if usuario['id'] == id:
            usuarios[indice] = usuario_atualizado
            usuarios.sort(key=lambda x: x['id'])
            return usuario_atualizado

def criar_usuario(usuario_novo):
    '''Cria um novo usuario na base de dados'''
    for usuario in usuarios:
        if usuario['id'] == usuario_novo['id']:
            return None        
    usuarios.append(usuario_novo)
    usuarios.sort(key=lambda x: x['id'])
    return usuario_novo

def deletar_usuario(id):
    '''Deleta um usuario que o id for correspondente'''
    for indice,usuario in enumerate(usuarios):
        if usuario['id'] == id:
            del usuarios[indice]
            return usuarios
    return None