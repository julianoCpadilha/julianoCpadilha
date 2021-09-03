class Agenda:
    def __init__(self, nome_proprietario, ano):
        self.__nome_proprietario = nome_proprietario
        self.__ano = ano

    def setNome_proprietario(self, nome_proprietario):
        self.__nome_proprietario = nome_proprietario

    def getNome_proprietario(self):
        return self.__nome_proprietario

    def setAno(self, ano):
        self.__ano = ano

    def getAno(self):
        return self.__ano
