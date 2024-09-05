"""
SOMANDO NÚMEROS
"""

soma = 0

while True:
    numero = int(input("Digite um número (negativo para parar): "))
    if numero < 0:
        break
    soma += numero

print(f"Soma total: {soma}")