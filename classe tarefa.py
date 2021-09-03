class Tarefa:
    def __init__(self, descricao, status):
        self.__descricao = descricao
        self.__status = status

    def setDescricao(self, descricao):
        self.__descricao = descricao

    def getDescricao(self):
        return self.__descricao

    def setStatus(self, status):
        self.__status = status

    def getStatus(self):
        return self.__status