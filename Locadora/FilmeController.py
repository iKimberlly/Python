
from conexao import Conexao
from FilmeModel import FilmeModel

class FilmeController:
    
    def __init__(self, view):
        self.view = view
        self.__conn = Conexao().conect()  
        self.gerarTabela()
    
    def gerarTabela(self):
        try:
            self.__conn.execute('''
                CREATE TABLE IF NOT EXISTS filme (
                    codigo INTEGER NOT NULL PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    disponivel VARCHAR(150) NOT NULL
                )
            ''')
            self.__conn.commit()
        except Exception as e:
            print(f"Erro na criação da tabela: {e}")
        finally:
            self.__conn.close()  

    def inserir(self):
        codigo = self.view.codigo.get()
        nome = self.view.nome.get()
        disponivel = self.view.disponivel.get()
        
        if not codigo.isdigit() or not nome or not disponivel:
            return False

        obj = FilmeModel()
        obj.setcodigo(int(codigo))
        obj.setNome(nome)
        obj.setdisponivel(disponivel)

        try:
            conn = Conexao().conect()
            conn.execute("INSERT INTO filme (codigo, nome, disponivel) VALUES (?, ?, ?)",
                         (obj.getcodigo(), obj.getNome(), obj.getdisponivel()))
            conn.commit()
            return True
        except Exception as e:
            print(f"Erro: {e}")
            return False
        finally:
            conn.close() 
