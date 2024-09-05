"""
CONTAR VOGAIS
"""
while True:
    palavra = input("Digite uma palavra (ou pressione Enter para sair): ")
    if palavra == "": # Se não tiver palavras, por isso ENTER direto.
        break # Se não conter nenhuma palavra então para.

    vogais = "aeiouAEIOU" # Estou aprendendoo algoritmo a reconhecer vogais.
    contagem_vogais = sum(1 for letra in palavra if letra in vogais) 
    """
    A variável contagem_vogais contém uma função de soma (sum) que atribui o número 1
    para cada vogal presente na variável vogais para de depois somar.
    """
    
    print(f"A palavra '{palavra}' tem {contagem_vogais} vogais.")