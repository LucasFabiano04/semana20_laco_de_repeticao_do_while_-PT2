"""
ADIVINHE O NÚMERO SECRETO
"""

import random

numero_secreto = random.randint(1, 100)
adivinhou = False

while True:
    palpite = int(input("Adivinhe o número (entre 1 e 100): "))
    if palpite == numero_secreto:
        print("Parabéns, você acertou!✔")
        break
    else:
        print("Tente novamente!❌")