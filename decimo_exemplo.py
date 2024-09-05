"""
CALCULANDO A MÉDIA DAS NOTAS
"""

soma = 0
contagem = 0

while True:
    nota = float(input("Digite uma nota (ou -1 para terminar): "))
    if nota == -1: #se digitar -1
        break # então o programa encerra e calcula a nota
    soma += nota # somar 0 + o número digitado pelo usuário
    contagem += 1 # CONTA A QUANTIDADE de notas para calcular a média.

if contagem > 0: # Se tiver alguma nota
    media = soma / contagem # A variável média recebe o cálculo da soma das notas pela quantidade de notas
    print(f"A média das notas é: {media:.2f}") # Arredondando resultado para até 2 casas decimais após a vírgula
else:
    print("Nenhuma nota foi inserida.")