"""
TABUADA
"""

while True: 
    numero = int(input("Digite um número para ver a tabuada (0 para sair): "))
    if numero == 0: # Se o número digitado for 0
        break # O programa para quando digitamos o zero
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")