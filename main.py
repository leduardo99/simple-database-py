import pymysql
import time

try:
    conect = pymysql.connect(host="localhost",
                             user="root",
                             password="",
                             database="bd")
    print("[*] Conectado com o banco ...")
    time.sleep(3)
    print('[*] Conectado com sucesso')
except:
    print("Não foi possível conectar com o banco de dados.")


def logarSistema():
    rlogin = str("login")
    rsenha = str("senha")
    usuario = txtUsuario.get()
    senha = txtSenha.get()

    try:
        rs = conect.cursor()
        rs.execute("SELECT * FROM tbl_user WHERE usuario='{}'".format(usuario))
        for linha in rs:
            rlogin = linha[1]
            rsenha = linha[2]
        rs.close()
        if usuario == rlogin and senha == rsenha:
            janela.destroy()
            abrirJanela2()
        else:
            lblMensagem['text'] = "Usuario/Senha incorreto"
    except:
        lblMensagem['text'] = "Erro na autenticação"


def cadastrarUsuario():
    cursor = conect.cursor()
    login = txtUsuario.get()
    senha = txtSenha.get()
    sql = "INSERT INTO tbl_user(usuario, senha) VALUES (%s, %s)"
    cursor.execute(sql, (login, senha))
    conect.commit()
    conect.close()
    print("[*] Cadastrado com sucesso, conecte-se novamente para logar-se")
    
    
    
###########################################################################################################################################################

#Testes

login = str()
senha = str()
rlogin = str()
rsenha = str()
escolha = '0'


def cls():
    print("\n" * 100)


try:
    conect = pymysql.connect(host="localhost",
                             user="root",
                             password="",
                             database="testes")
    print("[*] Conectado com o banco ...")
    time.sleep(3)
    print('[*] Conectado com sucesso')
    print('[*] Limpando tela ...')
except:
    print("Não foi possível conectar com o banco de dados.")

while escolha != '-1':
    print("""   LISTA DE COMANDOS
    [1] - Login
    [2] - Cadastrar
    [3] - Gerar relatório de conexões
    [0] - Sair
    """)
    escolha = input("Opção desejada: ")

    if escolha == '1':
        cursor = conect.cursor()
        print('==================== TELA DE LOGIN ====================')
        login = input("                   Digite seu login: ")
        senha = input("                   Digite sua senha: ")
        print('=======================================================')

        sql = "SELECT * FROM tbl_user WHERE usuario='%s'"
        cursor.execute(sql % login)
        conect.close()

        for linha in cursor:
            rlogin = linha[1]
            rsenha = linha[2]
        cls()
        break
    elif escolha == '2':
        cursor = conect.cursor()
        print('==================== TELA DE CADASTRO ====================')
        login = input("                   Digite seu login: ")
        senha = input("                   Digite sua senha: ")
        print('==========================================================')
        sql = "INSERT INTO tbl_user(usuario, senha) VALUES (%s, %s)"
        cursor.execute(sql, (login, senha))
        conect.commit()
        conect.close()
        print("[*] Cadastrado com sucesso, conecte-se novamente para logar-se")
        sys.exit(0)
    else:
        sys.exit(0)

if login == rlogin:
    print('Logado com sucesso')
else:
    print('Usuario nao cadastrado')
print("[*] Programa finalizado")