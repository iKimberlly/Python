
class FilmeModel:
    
    def __init__(self):
        self.__codigo = None
        self.__nome = None
        self.__disponivel = None

    def setcodigo(self, codigo):
        self.__codigo = codigo

    def getcodigo(self):
        return self.__codigo

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setdisponivel(self, disponivel):
        self.__disponivel = disponivel

    def getdisponivel(self):
        return self.__disponivel
    
    def toMaps(self):
        return {
            'codigo': self.getcodigo(),
            'nome': self.getNome(),
            'disponivel': self.getdisponivel()
        }
