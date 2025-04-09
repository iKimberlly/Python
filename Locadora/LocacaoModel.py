
class LocacaoModel:

    def __init__(self):
        self.__id = None
        self.__matricula = None
        self.__nome = None
        self.__contato = None
        self.__filme = None
        self.__data_locacao = None
        self.__data_devolucao = None

    def setId(self, id):
        self.__id = id
    def getId(self):
        return self.__id

    def setMatricula(self, matricula):
        self.__matricula = matricula
    def getMatricula(self):
        return self.__matricula

    def setNome(self, nome):
        self.__nome = nome
    def getNome(self):
        return self.__nome

    def setContato(self, contato):
        self.__contato = contato
    def getContato(self):
        return self.__contato
    
    def setFilme(self, filme):
        self.__filme = filme
    def getFilme(self):
            return self.__filme
        
    def setDataLocacao(self, data_locacao):
        self.__data_locacao = data_locacao
    def getDataLocacao(self):
        return self.__data_locacao
    
    def setDataDevolucao(self, data_devolucao):
        self.__data_devolucao = data_devolucao
    def getDataDevolucao(self):
        return self.__data_devolucao

    def toMaps(self):
        return {
            'id': self.getId(),
            'nome': self.getNome(),
            'contato': self.getContato(),
            'filme': self.getFilme(),
            'data_locacao': self.getDataLocacao(),
            'data_devolucao': self.getDataDevolucao()
        }