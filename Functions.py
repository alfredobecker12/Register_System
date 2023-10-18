import string
import os

registeredUsers = {}

def passwordCheck(password):
    upperscore = 0
    alphascore = 0
    numscore = 0
    specialscore = 0
    
    if (12 >= len(password) >= 8):
        for i in password:
            if i.isdigit():
                numscore += 1
            elif i.isalpha() and i.isupper():
                upperscore += 1
                alphascore += 1
            elif i.isalpha():
                alphascore += 1
            elif i in list(string.punctuation):
                specialscore += 1
        
        if upperscore and alphascore and numscore and specialscore > 0:
            print("\nA senha é segura.")
            return True
        else:
            print("\nSenha informada não está atendendo os padrões de segurança. Tente novamente.")
            return False
    else:
        print("\nTamanho de senha inválido.")
        return False


def register():
    os.system("cls")
    print("Insira seu login: ")
    tempUser = input()
    while True:
        tempPass = input("\nInsira sua senha seguindo os seguintes parâmetros:\n.8 - 12 Caracteres\n.1 Caractere maiúsculo\n.1 Caractere especial.\nSenha: ")

        if passwordCheck(tempPass):
            break
    while True:
        print("\nConfirme a senha: ")
        tempPassConfirmation = input()
        if tempPassConfirmation == tempPass:
            break
        print("\nSenha incorreta.\n")

    registeredUsers.update({tempUser:tempPass})
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
    os.system("cls")
    while True:
        tempUser = input("\nUsuário: ")
        if tempUser == "sair":
            return
        if tempUser in registeredUsers.keys():
            break
        print("Usuário não encontrado, digite novamente. (Digite sair para voltar ao menu)\n")    
    
    cont = 3
    while True:
        tempPassword = input("\nSenha: ")
        if tempPassword == registeredUsers.get(tempUser):
            print("\nVocê está logado!")
            break
        cont -= 1
        if cont == 0:
            print("Tentativas esgotadas, sistema finalizado.")
            exit()
        print(f"\nSenha Incorreta. Tente novamente ({cont} tentativas restantes).\n")

        
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
            
