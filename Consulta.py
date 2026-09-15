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



