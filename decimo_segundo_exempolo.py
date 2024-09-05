"""
CONTAGEM REGRESSIVA
"""
while True:
    numero = int(input("Digite um número para iniciar a contagem regressiva: "))
    
    while numero >= 0: # Enquanto for maior que zero
        print(numero) # Mostre o número
        numero -= 1 # Na ordem decrescente
    
    continuar = input("Quer fazer outra contagem regressiva? (s/n): ")
    if continuar.lower() == 'n': # Se digitar a letra n
        break # Vai parar