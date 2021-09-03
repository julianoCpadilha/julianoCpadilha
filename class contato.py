class Contato:
    def __init__(self, cpf, nome, email):
        self.__cpf = cpf
        self.__nome = nome
        self.__email = email

    def setCpf(self, cpf):
        self.__cpf = cpf

    def getCpf(self):
        return self.__cpf

    def setContato(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setEmail(self, email):
        self.__email = email

    def getEmail(self):
        return self.__email