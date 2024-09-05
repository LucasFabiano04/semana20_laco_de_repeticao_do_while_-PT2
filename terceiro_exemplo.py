"""
DIGITE A SENHA CORRETA
"""
senha_correta = "turma2b"

while True:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Senha correta! Acesso concedido ✔.")
        break
    else:
        print("Senha incorreta!❌ Tente novamente.")