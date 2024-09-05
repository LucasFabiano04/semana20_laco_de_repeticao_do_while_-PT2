"""
JOGO DO PAR OU ÍMPAR
"""

import random

while True:
    escolha = input("Escolha par ou ímpar (ou digite 'sair' para terminar): ").lower()
    if escolha == "sair":
        break
    
    numero_usuario = int(input("Digite um número: "))
    numero_computador = random.randint(1, 10)
    resultado = numero_usuario + numero_computador
    
    print(f"Você escolheu {numero_usuario}, e o computador escolheu {numero_computador}. A soma é {resultado}.")
    
    if (resultado % 2 == 0 and escolha == "par") or (resultado % 2 != 0 and escolha == "ímpar"):
        print("Você ganhou!")
    else:
        print("Você perdeu!")