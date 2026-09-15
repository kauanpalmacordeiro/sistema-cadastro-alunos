
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