while True:
    # Come um pedaço de bolo (faz alguma coisa)
    print("Comi um pedaço de bolo")
    
    # Verifica se ainda tem bolo
    tem_bolo = input("Ainda tem bolo? (s/n) ")
    
    # Se não tiver mais bolo, paramos
    if tem_bolo.lower() == 'n':
        break