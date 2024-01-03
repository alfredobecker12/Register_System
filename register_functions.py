import string
import os
import random
import sql_functions as sqf

def passwordCheck(password):
    upper = False
    alpha = False
    num = False
    special = False
    
    if (20 >= len(password) >= 8):
        for i in password:
            if i.isdigit():
                num = True
            elif i.isupper():
                upper = True
                alpha = True
            elif i.isalpha():
                alpha = True
            elif i in list(string.punctuation):
                special = True
        
        if upper and alpha and num and special:
            return True
        else:
            print("\nSenha informada não está atendendo os padrões de segurança. Tente novamente.")
            return False
    else:
        print("\nTamanho de senha inválido.")
        return False


def userCheck(username):
    if len(username) < 6:
            print("Tamanho inválido.")
            return None
    
    if sqf.checkUser(username):
        suggestions = []
        while len(suggestions) != 3:
            suggestion = username + str(random.randrange(10, 1000))
            if not sqf.checkUser(suggestion):
                suggestions.append(suggestion)
        print("\nUsuário já existente. Tente outro ou escolha uma das sugestões abaixo\n")
        for i in range(len(suggestions)):
            print(f"{i+1}. {suggestions[i]}\n")
        option = input("4. Tentar outro username\n")
        
        if option == "1":
            return suggestions[0]
        elif option == "2":
            return suggestions[1]
        elif option == "3":
            return suggestions[2] 
        elif option == "4":
            return None
        
        else:
            print("Opção inválida. Tente realizar o cadastro novamente.")
            return None
    else:
        return username


def register():
    while True:
        tempUser = input("\nInsira seu username de no mínimo 6 caracteres: ")
        username = userCheck(tempUser)
        if username is None:
            continue
        else:
            break
    
    while True:
        tempPass = input("\nInsira sua senha seguindo os seguintes parâmetros:\n.8 - 20 Caracteres\n.1 Caractere maiúsculo\n.1 Caractere especial\n.1 Caractere Numérico\nSenha: ")
        if passwordCheck(tempPass):
            break
    while True:
        print("\nConfirme a senha: ")
        tempPassConfirmation = input()
        if tempPassConfirmation == tempPass:
            break
        print("\nSenha incorreta.\n")

    sqf.insertUserData(username, tempPass)

    return


def homePage():
    os.system("cls")
    print("                        Bem Vindo ao sistema de login do Alfredo\n\n")
    print("                                      Opções:\n")
    print("                                     1. Login\n")
    print("                                     2. Cadastro\n")
    print("                                     3. Sair\n\n")
    option = input("                                     Opção: ")
    return option


def login():
    cont = 3
    os.system("cls")
    while True:
        username = input("\nUsuário: ")
        if username == "sair":
            return False
        password = input("\nSenha: ")
        if sqf.checkLogin(username, password):
            print("Usuário logado.")
            return True
        else:
            cont -= 1
            print(f"\n{cont} Tentativas restantes.")
            if cont == 0:
                return False


def main():
    while True:
        optionSelected = homePage()
        
        if optionSelected == '1':
            login()
        elif optionSelected == '2':
            register()
        elif optionSelected == "3":
            os.system("cls")
            exit() 

