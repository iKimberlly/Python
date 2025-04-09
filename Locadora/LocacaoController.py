from conexao import Conexao
from LocacaoModel import LocacaoModel

class LocacaoController:

    def __init__(self, view):
        self.view = view
        self.__conn = Conexao().conect()  
        self.gerarTabela()

    def gerarTabela(self):
        try:
            self.__conn.execute('''
                CREATE TABLE IF NOT EXISTS locacao (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    matricula INTEGER NOT NULL,
                    nome VARCHAR(100) NOT NULL,
                    filme VARCHAR(100) NOT NULL,
                    data_locacao DATE NOT NULL,
                    data_devolucao DATE
                    FOREIGN KEY (id) REFERENCES cliente (matricula)
                )
            ''')
            self.__conn.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.__conn.close()

    def inserir(self):
        id = self.view.codigo.get()
        matricula = self.view.matricula.get()
        nome = self.view.nome.get()
        filme = self.view.filme.get()
        data_locacao = self.view.data_locacao.get()
        data_devolucao = self.view.data_devolucao.get()

        if not matricula.isdigit() or not nome or not filme:
            return False

        obj = LocacaoModel()
        obj.setId(int(id) if id else None)  
        obj.setMatricula(int(matricula))
        obj.setNome(nome)
        obj.setFilme(filme)
        obj.setDataLocacao(data_locacao)
        obj.setDataDevolucao(data_devolucao)

        try:
            conn = Conexao().conect()
            conn.execute('''
                INSERT INTO locacao (matricula, nome, filme, data_locacao, data_devolucao) 
                VALUES (?, ?, ?, ?, ?)
            ''', (obj.getMatricula(), obj.getNome(), obj.getFilme(), obj.getDataLocacao(), obj.getDataDevolucao()))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()
