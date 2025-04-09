# ClienteModel.py
class ClienteModel:

    def __init__(self):
        self.__matricula = None
        self.__nome = None
        self.__contato = None

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
