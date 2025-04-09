from conexao import Conexao
from ClienteModel import ClienteModel

class ClienteController:

    def __init__(self, view):
        self.view = view
        self.__conn = Conexao().conect()  
        self.gerarTabela()

    def gerarTabela(self):
        try:
            self.__conn.execute('''
                CREATE TABLE IF NOT EXISTS cliente (
                    matricula INTEGER NOT NULL PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    contato VARCHAR(150) NOT NULL
                )
            ''')
            self.__conn.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.__conn.close()  

    def inserir(self):
        matricula = self.view.matricula.get()
        nome = self.view.nome.get()
        contato = self.view.contato.get()

        if not matricula.isdigit() or not nome or not contato:
            return False

        obj = ClienteModel()
        obj.setMatricula(int(matricula))
        obj.setNome(nome)
        obj.setContato(contato)

        try:
            conn = Conexao().conect()
            conn.execute("INSERT INTO cliente (matricula, nome, contato) VALUES (?, ?, ?)",
                         (obj.getMatricula(), obj.getNome(), obj.getContato()))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close() 
