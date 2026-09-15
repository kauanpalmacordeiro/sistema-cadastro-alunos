//Cadastro 


usuarios = []

print("=== CADASTRO ===")

nome = input("Nome: ")
email = input("Email: ")
senha = input("Senha: ")

usuario = {
    "nome": nome,
    "email": email,
    "senha": senha
}

usuarios.append(usuario)

print("Usuário cadastrado!")
print(usuarios)

//Consulta


print("=== CONSULTA ===")

nome_consulta = input("Digite o nome para consultar: ")

for usuario in usuarios:
    if usuario["nome"] == nome_consulta:
        print("Usuário encontrado!")
        print("Nome:", usuario["nome"])
        print("Email:", usuario["email"])
        print("Senha:", usuario["senha"])
        break
else:
    print("Usuário não encontrado!")



//Exclusão


usuarios = [
    {
        "nome": "Carlos",
        "email": "carlos@email.com",
        "senha": "123"
    }
]

print("=== EXCLUSÃO ===")

email = input("Digite o email do usuário: ")

for usuario in usuarios:
    if usuario["email"] == email:
        usuarios.remove(usuario)
        print("Usuário excluído!")
        print(usuarios)
        break
else:
    print("Usuário não encontrado!")