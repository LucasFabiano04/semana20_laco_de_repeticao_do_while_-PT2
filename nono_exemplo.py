"""
LOGIN SIMPLES
"""
"""
no inicio do algoritmo determinamos intruções e funções, para depois determinar
INPUTS, PRINTS, CONDIÇÕES, ESTRUTURAS DE SELEÇÃO, ESTRUTURA DE
"""

usuario_correto = "admin" # O usuário deverá ser este
senha_correta = "1234" # A senha deverá ser esta

while True: # Enquanto estiver na lista (Enquanto for verdadeiro)
    usuario = input("Nome de usuário: ") # recebe o usuário
    senha = input("Senha: ") # recebe a senha
    
    if usuario == usuario_correto and senha == senha_correta: # Se o usuário *E* e a senha estiverem corretos
        print("Login bem-sucedido!") # Se estiver correto o sistema para. 
        break   #Então, caso contrário, por outro lado...
    else: # Se não, caso contrário, por outro lado...
        print("Usuário ou senha incorretos! Tente novamente.") # O usuário tentará novamente.