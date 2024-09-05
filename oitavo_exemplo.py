"""
ESCOLHENDO A OPÇÃO
"""

while True:
    print("\nMenu:")
    print("1. Pizza")
    print("2. Esfiha")
    print("3. Kibe")
    print("4. Coxinha")
    print("0. Sair")
    
    escolha = input("Escolha uma opção: ") # A variável escolha receberá o dado digitado pelo usuário
    
    if escolha == '0': # Se a escolha for igual a 0
        print("Saindo...") # Mostrar saindo
        break # O programa foi interrompido de acordo com a condição
    elif escolha == '1':
        print("Você escolheu a Opção 1!")
    elif escolha == '2':
        print("Você escolheu a Opção 2!")
    elif escolha == '3':
        print("Você escolheu a Opção 3!")
    elif escolha == '4':
        print("Você escolheu a Opção 4!")
    else:
        print("Opção inválida! Tente novamente.")
