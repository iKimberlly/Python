import getpass
import datetime

def login():
  login = input("Digite seu login: ")
  with open("usuarios.txt","r") as arquivos:
   for linha in arquivos.readlines():
      login_salvo = linha.strip().split(",")
      if login == login_salvo:
        print("Login efetuado com sucesso!")
        return True
  print("Login ou senha errado")
  return False

def senha():
  senha = input("Digite sua senha: ")
  with open("usuarios.txt","r") as arquivos:
    for linha in arquivos.readlines():
      senha_salva = linha.strip().split(",")
      if senha == senha_salva[1]:
        print("Login efetuado com sucesso!")
        return True
    print("Login ou senha errado")
    return False
  
def senha_valida(senha, len_pass = 8):
    if len(senha) >= len_pass:
        print("Senha registrado com sucesso")
    else:
        print("Senha invalido")

usuarios = []
def cad_usuario(usuarios):
    login = input("Digite seu nome de usuario: ")
    senha = input("Digite uma senha: ")
    with open("usuarios.txt", "a") as arquivos:
        arquivos.write(f"{login},{senha}\n")
    print("Usuario cadastrado com sucesso!\n")
    return "Erro no cadastro tente novamente"

novo_usuario = []
novo_usuario.append(usuarios)

def fazer_login():
  print("Usuario")
  login = input("Digite seu usuario: ")
  print("Senha")
  senha = getpass.getpass("Digite sua senha")
  with open("usuarios.txt", "r") as arquivos:
        for linha in arquivos:
           #verificar se a linha contem pelo menos dois valores separados por virgula
           login_salvo, senha_salva = linha.strip().split(",",1)

           if login == login_salvo and senha == senha_salva:
            print("Login efetuado com sucesso!")
            return True

        print("Usuarios nao encotrado! Tente novamente.")
        return False
def redefinir_senhatest():
    login = input("Digite o nome de usuário que deseja inserir nova senha: ")
    usuarios = []

    # verificar se o usuário existe
    with open("usuarios.txt", "r") as arquivos:
        for linha in arquivos:
            usuario, senha_salva = linha.strip().split(",")
            usuarios.append((usuario, senha_salva))
    # o usuario_encontrado = none esta sendo usado para armazenar o índice do usuário no usuarios.txt se uma correspondência for encontrada
    usuario_encontrado = None
    for i, (usuario, senha_salva) in enumerate(usuarios):
        if login == usuario:
            usuario_encontrado = i
            break
      # se o usuário existe solicitar uma nova senha
    if usuario_encontrado is not None:
        nova_senha = input("Digite a nova senha: ")
        usuarios[usuario_encontrado] = (login, nova_senha)

        # reescrever a nova senha
        with open("usuarios.txt", "w") as arquivos:
            for usuario, senha_salva in usuarios:
                arquivos.write(f"{usuario},{senha_salva}\n")

        print(f'Senha redefinida com sucesso para o usuário {login}')
        return True
    else:
        print(f"Usuário {login} não encontrado")
        return False

def Visu_usuario():
    print("Visualizar usuários: ")
    with open("usuarios.txt", "r") as arquivo:
        for linha in arquivo:
          login_salvo, senha_salva = linha.strip().split(",")
          print(f"Usuário: {login_salvo}, Senha: {senha_salva}")
          data = datetime.datetime.today()
          dia = data.day
          mes = data.month
          ano = data.year

          print(f'{dia}/{mes}/{ano}')

def excluir_usuario():
    print("Excluir usuário:")
    login = input("Digite o nome de usuário que deseja excluir: ")
    # Verifica se o usuário existe
    with open("usuarios.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    for ler, linha in enumerate(linhas):
        login_salvo, senha_ = linha.strip().split(",")
        if login == login_salvo:
            del linhas[ler]

            with open("usuarios.txt", "w") as arquivo:
                arquivo.writelines(linhas)

            print("Usuário excluído com sucesso!\n")
            return

    print("Usuário não encontrado.\n")

def menu():
  while True:
    print("____MENU____")
    print("-- L _ Cadastrar Usuario --")
    print("-- E _ Fazer login --")
    print("-- T _ Redefinir senha --")
    print("-- S _ Visualizar Usuario --")
    print("-- G _ Excluir Usuario --")
    print("-- O _ Finalizar --")
    opcao = input("Escolha uma opção: ").upper() #para converter a entrada para maiúscula
    print()

    if opcao == "L":
      cad_usuario(usuarios)
    elif opcao == "E":
       if fazer_login():
          menu_logado()
    elif opcao == "T":
      redefinir_senhatest()
    elif opcao == "S":
       if Visu_usuario():
        data()
    elif opcao == "G":
      excluir_usuario()
    elif opcao == "O":
      print("Programa Encerrado")
      break
    else:
      print("Opcão Invalido")

def menu_logado():
  print("")
  print("--------------------------------------")
  print("___Seja bem-vindo__")
  print("Ao nosso aplicativo Way somos Girassol")
  print("--------------------------------------")
  print("")

menu()
