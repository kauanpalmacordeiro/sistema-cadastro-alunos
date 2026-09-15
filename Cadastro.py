
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