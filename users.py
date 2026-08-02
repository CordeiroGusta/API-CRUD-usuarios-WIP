#dados dos usuarios para esse projeto que é apenas para desenvolver conhecimento
usuarios = [
    {
        "id": 1,
        "usuario": "fulano",
        "email": "fulanonice@sememail.com",
        "telefone": "4112345678"
    },
    {
        "id": 2,
        "usuario": "ciclano",
        "email": "bacana@sememail.com",
        "telefone": "4187654321"
    },
    {
        "id": 3,
        "usuario": "billy",
        "email": "dev@sememail.com",
        "telefone": "4111223344"
    },
    {
        "id": 4,
        "usuario": "roberts",
        "email": "dataengineer@sememail.com",
        "telefone": "4188776655"
    }
]

#metodos
def listar_usuarios():
    return usuarios

def listar_usuarios_id(id):
    for usuario in usuarios:
        if usuario['id'] == id:
            return usuario
