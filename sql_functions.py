from db_connection import *


def insertUserData(username, password):
    try:
        with conn:
            with conn.cursor() as curs_insert_userdata:
                userquery = "INSERT INTO usuarios(username, password) VALUES(%s, %s)"
                curs_insert_userdata.execute(userquery, (username, password))

    except Exception as e:
        print(f"SQL error: {e}")
        conn.rollback()


def checkUser(username):
    try:
        with conn:
            with conn.cursor() as curs_userCheck:
                userquery = 'SELECT username FROM usuarios WHERE username=%s'
                curs_userCheck.execute(userquery, (username,))
                if curs_userCheck.fetchone() is None:
                    #USERNAME NAO REGISTRADO
                    return False
                else:
                    #USERNAME REGISTRADO
                    return True

    except Exception as e:
        print(f"SQL error: {e}")


def checkLogin(username, password):
    try:
        with conn:
            with conn.cursor() as curs_loginCheck:
                userquery = "SELECT username, password FROM usuarios WHERE username=%s"
                #MESMO QUE SÓ TENHA UM PARÂMETRO, O MÉTODO EXECUTE ESPERA UMA TUPLA
                aux = curs_loginCheck.execute(userquery, (username,))
                #RETORNA STRINGS DENTRO DE UMA TUPLA
                if aux is None:
                    print("Usuário não encontrado.")
                    return False
                
                tempuser, temppass = curs_loginCheck.fetchone()
                if username != tempuser:
                    print("\nNome de usuário incorreto.")
                    return False
                if password != temppass:
                    print("\nSenha incorreta.")
                    return False
                return True

    except Exception as e:
        print(f"SQL error: {e}")


if __name__ == "__main__":
     var = 'dd'
     checkUser(var)
